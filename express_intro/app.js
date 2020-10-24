const express = require('express')
const app = express()

const port = 30000

app.listen('/', (req,res)=>{
    res.send('Hello world!')
})

app.listen(port,'127.0.0.1', ()=>{
    console.log(`Example listenting at ${port}`)
})