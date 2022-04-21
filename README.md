# Unimake - Rate and Create
Gonzalo Prats, Hugo Chapado, Emmanuel Mora and Justin Thai

<!-- Menu -->
<details open="open">
  <summary>Menu</summary>
  <ol>
    <li><a href="#Description">Description</a></li>
    <li><a href="#Instructions to Run">Instructions to run</a></li>
    <li><a href="#Database">Database</a></li>
  </ol>
</details>

## Description
Unimake is a platform where they can find other students with similar interests and that, for a fact, work well with others. It offers a rating system that allows students to check how well a certain user has worked in past projects, so that they do not have to choose their teammate blindly.

## Instructions to run
	Firstly, install the following dependencies: bcryptjs, cookie-parser, 
	dot env, express, hbs, jsonwebtoken, mysql, nodemon, and node js using 
	npm install.  Then set up the database (we had our database stored 
	locally so you will need to make it).

## Database
	For the database, we used MAMP (https://www.mamp.info/en/windows/) 
	to access a database locally.  Download this, and go to the preferences
	and change the Apache port to 8888 and MySQL port to 3306.  Run the application. 
	(You also need to create the database since it is only run locally, the database is named 
	Unimake-login, with 4 columns for Name, email, ID,and password).

	After, you run the code using npm start.  Then go to localhost:3000 for the website.
