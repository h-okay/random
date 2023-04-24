const buttonColours = ["red", "blue", "green", "yellow"];
let gamePattern = [];
let userClickedPattern = [];
let started = false;
let level = 0;

function nextSequence(max = 3) {
    userClickedPattern = [];
    const randomNumber = Math.floor(Math.random() * (max + 1));
    const randomColor = buttonColours[randomNumber];
    gamePattern.push(randomColor);
    $("#level-title").text("Level " + level++);
    $("#" + randomColor).fadeIn(100).fadeOut(100).fadeIn(100);
    playSound(randomColor);
}

function playSound(name) {
    let audio = new Audio(`sounds/${name}.mp3`);
    audio.play();
}

function animatePress(currentColor) {
    const id = "#" + currentColor;
    $(id).addClass("pressed");
    setTimeout(() => {
        $(id).removeClass("pressed");
    }, 100);
}

function startOver() {
    level = 0;
    gamePattern = [];
    started = false;
}

function checkAnswer(currentLevel) {
    if (gamePattern[currentLevel] === userClickedPattern[currentLevel]) {
        if (userClickedPattern.length === gamePattern.length) {
            setTimeout(nextSequence, 1000);
        }
    } else {
        $("body").addClass("game-over");
        setTimeout(() => { $("body").removeClass("game-over") }, 200);
        $("#level-title").text("Game Over, Press Any Key to Restart");
        playSound("wrong");
        startOver();
    }
}

$(document).keypress(() => {
    if (!started) {
        $("#level-title").text("Level " + level);
        nextSequence();
        started = true;
    }
});

$(".btn").click(function () {
    const chosenColor = $(this).attr("id");
    userClickedPattern.push(chosenColor);
    animatePress(chosenColor);
    playSound(chosenColor);
    checkAnswer(userClickedPattern.length - 1);
});
