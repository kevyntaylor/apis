//Vars and Const
var express = require('express');
var app = express();
var bodyParser = require('body-parser');
app.use(bodyParser.json());
const usersModel = require("./models/users");


//Endpoint Login REST DATA
app.post('/login', async function (req, res){
	usersModel.login(req.body.username,req.body.password).then(users => {
            res.json(users);
    })
    .catch(err => {
        return res.status(500).send("Error obteniendo user");
    });
});



app.listen(3000, function () {
	console.log('Sistema armado en el puerto 3000!');
});