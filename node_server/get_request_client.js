const http = require('http')
const querystring = require('querystring')

const parameters = {
    id: '123',
    msg: 'yoyo honey singh'
}

const get_request_args = querystring.stringify(parameters)

const options = {
    url: "http://10.10.136.133",
    port: "8000",
    method: "GET",
    path: "/?" + get_request_args,
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
}

const request = http.request(options, (response) => {
    //response from server
})

// request.on('error', (error) => {
//     console.log("error")
// })

request.end()