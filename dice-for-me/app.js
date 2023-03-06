function setDiceImage (imgNumber) {
  const dice = Math.floor(Math.random() * 6) + 1
  document
    .querySelector(`img.img${imgNumber}`)
    .setAttribute('src', `./images/dice${dice}.png`)
  return dice
}

function showWinner (dice1, dice2) {
  let title
  if (dice1 > dice2) {
    title = '🚩 Player 1 Wins!'
  } else if (dice1 < dice2) {
    title = 'Player 2 Wins! 🚩'
  } else {
    title = 'Draw!'
  }
  document.querySelector('h1').innerHTML = title
}
function main () {
  const dice1 = setDiceImage(1)
  const dice2 = setDiceImage(2)
  showWinner(dice1, dice2)
}

main()
