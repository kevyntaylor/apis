const connection = require("../config/data")
const bcrypt = require('bcrypt');
const saltRounds = 10;
//Open conection
connection.connect();

module.exports = {
    login(username, password) {
        return new Promise((resolve, reject) => {
            var usr = username;
			var pwd = password;
			connection.query('SELECT * FROM users WHERE username = ?', [usr], function(err, rows) {
				var pass = rows[0].password;
				bcrypt.compare(pwd, pass, function(err, result) {
				    if(result){
				    	resolve(rows);
				    }else{
				    	resolve({code:401,message: 'datos incorrectos'});
				    }
				});
				
			});
        });
    }
}