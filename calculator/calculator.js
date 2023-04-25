const express = require('express')
const bodyParser = require('body-parser')

const app = express()
app.use(bodyParser.urlencoded({ extended: true }))

app.get('/', function (_, res) {
  res.sendFile(__dirname + '/index.html')
})

app.post('/', function (req, res) {
  const n1 = parseInt(req.body.n1)
  const n2 = parseInt(req.body.n2)
  res.status(200).send('The result is ' + (n1 + n2))
})

app.get('/bmicalculator', function (_, res) {
  res.sendFile(__dirname + '/bmicalculator.html')
})

app.post('/bmicalculator', function (req, res) {
  const weight = parseInt(req.body.weight)
  const height = parseInt(req.body.height)
  const bmi = (weight / (height * height)) * 10000
  res.status(200).send('Your BMI is ' + bmi.toFixed(2))
})

app.listen(3000)
