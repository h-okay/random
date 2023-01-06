import math
import os
import random
from pathlib import Path

import pygame

# try:
#    os.environ["DISPLAY"]
# except:
#    os.environ["SDL_VIDEODRIVER"] = "dummy"

# setup pygame
pygame.init()
WIDTH, HEIGHT = 1280, 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")
FPS = 60
clock = pygame.time.Clock()

# fonts
LETTER_FONT = pygame.font.SysFont("comicsans", 40)
WORD_FONT = pygame.font.SysFont("comicsans", 90)
TITLE_FONT = pygame.font.SysFont("comicsans", 80)

# colors
WHITE = (180, 180, 180)
BLACK = (0, 0, 0)

# variables for buttons
RADIUS = 35
GAP = 15
A = 65


def random_word() -> str:
    """Gets a random word from the txt file."""
    path = os.path.join(Path(__file__).parent, "data", "randomwords.txt")
    with open(path, "r", encoding="utf-8") as file:
        words_need_filter = file.read().split("\n")
        words = list(filter((lambda x: len(x) <= 8), words_need_filter))
        word_ = random.choice(words)
        return word_


def message(msg):
    """Displays endgame screen"""
    pygame.time.delay(1500)
    window.fill(WHITE)
    text_ = WORD_FONT.render(msg, True, BLACK)
    window.blit(
        text_, (WIDTH / 2 - text_.get_width() / 2, HEIGHT / 2 - text_.get_height() / 2)
    )
    pygame.display.update()
    pygame.time.delay(3000)


def get_images() -> list:
    """Import all related assets"""
    images_ = []
    for i in range(7):
        img_path = os.path.join(Path(__file__).parent, "asset", f"hangman{i}.png")
        image = pygame.image.load(img_path)
        images_.append(image)
    return images_


def get_letters() -> list:
    """Returns a list of following for pygame drawn buttons and characters: x
    coordinate, y coordinate, character on the button, boolean for visibility
    """
    letters_ = []
    startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
    starty = 500
    for i in range(26):
        x_vec = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
        y_vec = starty + (i // 13) * (GAP + RADIUS * 2)
        letters_.append([x_vec, y_vec, chr(A + i), True])
    return letters_


def get_buttons() -> list:
    """Return a list of following for custom imported buttons: x coordinate, y
    coordinate, character on the button, boolean for visibility"""
    startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
    starty = 500
    buttons_ = []
    for i in range(26):
        button_path = os.path.join(
            Path(__file__).parent, "asset", "buttons", f"{i}.png"
        )
        x_vec = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
        y_vec = starty + (i // 13) * (GAP + RADIUS * 2)
        button = pygame.image.load(button_path)
        button = pygame.transform.smoothscale(button, (160, 160))
        buttons_.append([x_vec, y_vec, button, True])
    return buttons_


def draw(draw_word, draw_lives, draw_letters, draw_buttons, draw_images, draw_guessed):
    """Draws screen elements"""
    window.fill(WHITE)
    text_ = TITLE_FONT.render("HANGMAN", True, BLACK)
    window.blit(text_, (WIDTH / 2 - text_.get_width() / 2, 20))
    display_word = ""
    for letter in draw_word:
        if letter in draw_guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text_ = WORD_FONT.render(display_word, True, BLACK)
    window.blit(text_, (500, 200))
    for letter in draw_letters:
        x_vec, y_vec, ltr, visible = letter
        if visible:
            pygame.draw.circle(window, BLACK, (x_vec, y_vec), RADIUS, 1)
            text_ = LETTER_FONT.render(ltr, True, BLACK)
            window.blit(
                text_, (x_vec - text_.get_width() / 2, y_vec - text_.get_height() / 2)
            )
    for button in draw_buttons:
        pos_a, pos_b, but, visible = button
        if visible:
            window.blit(but, (pos_a - 80, pos_b - 80))
    window.blit(draw_images[draw_lives], (150, 100))
    pygame.display.update()


def main(main_run, main_lives, main_word, main_guessed, main_buttons, main_images):
    """Main game loop"""
    while main_run:
        clock.tick(FPS)
        draw(main_word, main_lives, letters, main_buttons, main_images, main_guessed)
        for evnt in pygame.event.get():
            # quit event
            if evnt.type == pygame.QUIT:
                main_run = False
            # click coord
            if evnt.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x_vec, y_vec, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x_vec - m_x) ** 2 + (y_vec - m_y) ** 2)
                        if dis < RADIUS:
                            main_guessed.append(ltr)
                            letter[3] = False
                            main_buttons[letters.index(letter)][3] = False
                            if ltr not in main_word:
                                main_lives += 1

        won = True
        for letter in main_word:
            if letter not in main_guessed:
                won = False
                break
        if won:
            message("WON")
            break
        if main_lives == 6:
            pygame.time.delay(1500)
            answr = f"The word was {main_word}"
            _text = WORD_FONT.render(answr, True, BLACK)
            window.fill(WHITE)
            window.blit(
                _text,
                (
                    WIDTH / 2 - _text.get_width() / 2,
                    HEIGHT / 2 - _text.get_height() / 2,
                ),
            )
            pygame.display.update()
            pygame.time.delay(1500)
            message("LOST")
            break


if __name__ == "__main__":
    # Playing the game
    while True:
        LIVES = 0
        guessed = []
        word = random_word()
        letters = get_letters()
        buttons = get_buttons()
        images = get_images()
        for event in pygame.event.get():
            ANSWER = "Click anywhere to play"
            text = WORD_FONT.render(ANSWER, True, BLACK)
            window.fill(WHITE)
            window.blit(
                text,
                (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2),
            )
            pygame.display.update()
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                RUN = True
                main(RUN, LIVES, word, guessed, buttons, images)
