from user import User
from words import Words


# create hidden game board
def board(arr):
    return (" __ " * len(arr)).split()


# game logic
USER = User()
PLAY = USER.ready()
while PLAY:
    # setup
    word = Words.random_word()
    game = board(word)
    LIFE = 10
    # play
    while ("__" in game) and (LIFE != 0):
        print(*game)
        guess = USER.user_input()

        if guess in game:
            print(f"{guess} already revealed.")
        else:
            indices = []
            for idx, wrd in enumerate(word):
                if wrd == guess:
                    indices.append(idx)
            if len(indices) == 0:
                LIFE -= 1
                print(f"Remaning LIFE: {LIFE}")
            for val in indices:
                game[val] = guess  # type: ignore

    if LIFE == 0:
        print("You are out of lives.")
        PLAY = USER.again()

    if ("__" not in game) and (LIFE != 0):
        print("You guessed it!")
        PLAY = USER.again()

print("Thank you for playing.")
