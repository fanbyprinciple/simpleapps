const fs = require('fs')
const ndjson = require('ndjson')
const express = require('express')
const app = express()
const port = 3000


let drawings = [];
fs.createReadStream('airplane.ndjson').pipe(ndjson.parse()).on('data', function(obj){
    // console.log(obj);
    drawings.push(obj);
})

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

app.use(express.static('public'))

app.get('/airplane', (req, res) => {
    const r = Math.floor(Math.random() * drawings.length)
    res.send(drawings[r])
})
