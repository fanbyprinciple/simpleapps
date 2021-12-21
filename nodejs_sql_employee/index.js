const express = require("express");
const mysql = require("mysql");

//create connection

const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
});

db.connect((err)=>{
    if (err){
        throw err;
    }
    console.log("Mysql connected")
})

const app = express()

app.get("/createdb", (req, res)=>{
    let sql ="CREATE DATABASE nodemysql";
    db.query(sql, (err)=>{
        if (err){
            throw err;
        }

        res.send("Database created")
    })
})

app.get("/createemployee", (req, res)=>{
    let sql = "CREATE TABLE employee(id int AUTO_INCREMENT, name VARCHAR(255), designation VARCHAR(255), PRIMARY KEY(id))"

    db.query(sql, (err)=>{
        if (err){
            throw err;
        }
        res.send("employee table created")
    })
})

// Insert employee 1

app.get("/employee1", (req, res) => {

  let post = { name: "Jake Smith", designation: "Chief Executive Officer" };

  let sql = "INSERT INTO employee SET ?";

  let query = db.query(sql, post, (err) => {

    if (err) {

      throw err;

    }

    res.send("Employee 1 added");

  });

});

//update employee
app.get("/updateemployee/:id", (req, res) => {

    let newName = "Updated name";
  
    let sql = `UPDATE employee SET name = '${newName}' WHERE id = ${req.params.id}`;
  
    let query = db.query(sql, (err) => {
  
      if (err) {
  
        throw err;
  
      }
  
      res.send("Post updated...");
  
    });
  
  });

// Delete employee

app.get("/deleteemployee/:id", (req, res) => {

    let sql = `DELETE FROM employee WHERE id = ${req.params.id}`;
  
    let query = db.query(sql, (err) => {
  
      if (err) {
  
        throw err;
  
      }
  
      res.send("Employee deleted");
  
    });
  
  });
  
   
  
app.listen("3000", () => {
  
    console.log("Server started on port 3000");
  
  });