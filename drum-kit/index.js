function listenAll (e) {
  document.addEventListener('keydown', handleKey),
  document
    .querySelector(`button.${e}`)
    .addEventListener('click', handleClick)
}
function changeBorder (e) {
  document.querySelector(`button.${e}`).classList.add('pressed'),
  setTimeout(() => {
    document.querySelector(`button.${e}`).classList.remove('pressed')
  }, 100)
}
function getSoundEffect (e) {
  let t = null
  switch (e) {
    case 'w':
      t = 'tom-1'
      break
    case 'a':
      t = 'tom-2'
      break
    case 's':
      t = 'tom-3'
      break
    case 'd':
      t = 'tom-4'
      break
    case 'j':
      t = 'snare'
      break
    case 'k':
      t = 'crash'
      break
    case 'l':
      t = 'kick-bass'
      break
    default:
  }
  return t
}
function playSound (e) {
  new Audio(`sounds/${e}.mp3`).play()
}
function handleClick (e) {
  const t = e.target.classList[0]
  const n = getSoundEffect(t)
  changeBorder(t), playSound(n)
}
function handleKey (e) {
  const t = e.key
  const n = getSoundEffect(t)
  changeBorder(t), playSound(n)
}
function main () {
  ['w', 'a', 's', 'd', 'j', 'k', 'l'].forEach(listenAll)
}
main()
