const express = require("express");
const https = require("https");
const bodyParser = require("body-parser");
const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

const appid = ""; // api key

app.get("/", function (_, res) {
    res.sendFile(__dirname + "/index.html");
});

app.post("/", function (req, res) {
    const locationUrl = `https://api.openweathermap.org/geo/1.0/direct?q=${req.body.city}&appid=${appid}`;
    https.get(locationUrl, function (response) {
        response.on("data", function (data) {
            const locationData = JSON.parse(data);
            const lat = locationData[0].lat;
            const lon = locationData[0].lon;
            const url = `https://api.openweathermap.org/data/2.5/weather?appid=${appid}&lat=${lat}&lon=${lon}&units=metric`;
            https.get(url, function (innerResponse) {
                innerResponse.on("data", function (innerData) {
                    const weatherData = JSON.parse(innerData);
                    const temp = weatherData.main.temp;
                    const desc = weatherData.weather[0].description;
                    const img = weatherData.weather[0].icon;
                    const imgUrl = "https://openweathermap.org/img/wn/" + img + "@2x.png";
                    res.write('<head><meta charset="utf-8"></head>');
                    res.write("<img src=" + imgUrl + ">");
                    res.write(`<h1>${req.body.city} currently has ` + desc + " and the temperature is " + temp + "</h1>");
                    res.send();
                })
            });
        })
    });
});


app.listen(3000);
