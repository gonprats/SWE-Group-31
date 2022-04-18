const express = require("express");
const path = require('path');
const mysql = require("mysql");
const dotenv = require("dotenv");


//tells dotenv where file is that has variables (host, user, ...)
dotenv.config({ path: './.env'});

const app = express();

const db = mysql.createConnection({
    //since locally hosted for now, host is localhost, later it should be ip address 
    //password for xamp is '', mamp is 'root'

    //instead of host: 'localhost', use process.env.DATABASE_HOST for protection
    host: process.env.DATABASE_HOST, 
    user: process.env.DATABASE_USER,
    password: process.env.DATABASE_PASSWORD,
    database: process.env.DATABASE
});

//__dirname is a var from nodejs that gives access to current directory of file
const publicDirectory = path.join(__dirname, './public');
app.use(express.static(publicDirectory));

//parses url-encoded bodies ???
app.use(express.urlencoded({ extended: false}));
//makes sure values from login form is sent as json format
app.use(express.json());


app.set('view engine', 'hbs');

db.connect( (error) => {
    if (error) {
        console.log(error)
    }
    else {
        console.log("MYSQL connected")
    }
})

// when on homepage (https:website/), it will run function with request, and response 
// request is what you want to grab from backend like data
// response is what you send to front end.

//ROUTES
app.use('/', require('./routes/pages'));
//whenever you go to /auth, require, /routes/auth
app.use('/auth', require('./routes/auth'));

//


/*
// this is called a route.
app.get("/", (req, res) => {
    // when you go to homepage/ you want to render index.hbs
    //res.render("index");
    res.render("index");
})

app.get("/register", (req, res) => {
    res.render("register");
})
*/


// port?
app.listen(3000, () => {
    console.log("Server started on port 3000")
})