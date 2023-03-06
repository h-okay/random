function setDiceImage (e) {
  const n = Math.floor(6 * Math.random()) + 1
  return (
    document
      .querySelector(`img.img${e}`)
      .setAttribute('src', `./images/dice${n}.png`),
    n
  )
}
function showWinner (e, n) {
  let t;
  (t = e > n ? '🚩 Player 1 Wins!' : e < n ? 'Player 2 Wins! 🚩' : 'Draw!'),
  (document.querySelector('h1').innerHTML = t)
}
function main () {
  showWinner(setDiceImage(1), setDiceImage(2))
}
main()
