const mysql = require("mysql");
const jwt = require("jsonwebtoken");
const bcrypt = require("bcryptjs");


const db = mysql.createConnection({
    host: process.env.DATABASE_HOST, 
    user: process.env.DATABASE_USER,
    password: process.env.DATABASE_PASSWORD,
    database: process.env.DATABASE
});

exports.register = (req, res) => {
    console.log(req.body);

    /*
    const name = req.body.name;
    const email = req.body.email;
    const password = req.body.password;
    const confirmPassword = req.body.confirmPassword;
    */
    //the same as above
    const { name, email, password, confirmPassword } = req.body;

    //now query to database
    db.query('SELECT email FROM users WHERE email = ?', [email], async (error, results) => {
        if (error) {
            console.log(erorr);
        }
        if(results.length > 0) {
            return res.render('register', {
                message: 'Email is already in use'
            })
        }
        else if (password !== confirmPassword) {
            return res.render('register', {
                message: 'The passwords do not match'
            })
        }

        let hashedPassword = await bcrypt.hash(password, 8);
        console.log(hashedPassword);

        db.query('INSERT INTO users SET ?', {name: name, email: email, password: hashedPassword}, (error, results) => {
            if(error) {
                console.log(error);
            }
            else {
                console.log(results);
                return res.render('register', {
                    message: 'User registered'
                })
            }
        });
    });
    res.send("Form submitted");
}