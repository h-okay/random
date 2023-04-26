const express = require("express")
const bodyParser = require("body-parser")
const rateLimit = require('express-rate-limit')
const app = express()


var limiter = rateLimit({
    windowMs: 1 * 60 * 1000, // 1 minute
    max: 5
})

app.use(limiter)
app.use(bodyParser.urlencoded({ extended: true }))


app.get("/", function (_, res) {
    res.sendFile(__dirname + "/index.html");
});

app.post("/", function (req, res) {
    let n1 = parseInt(req.body.n1);
    let n2 = parseInt(req.body.n2);
    res.status(200).send("The result is " + (n1 + n2));
})

app.get("/bmicalculator", function (_, res) {
    res.sendFile(__dirname + "/bmicalculator.html");
});

app.post("/bmicalculator", function (req, res) {
    const weight = parseInt(req.body.weight);
    const height = parseInt(req.body.height);
    const bmi = weight / (height * height) * 10000;
    res.status(200).send("Your BMI is " + bmi.toFixed(2));

})

app.listen(3000);
