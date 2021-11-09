var http = require('http');

var option = {
    hostname: "localhost",
    port: 8000,
    method: "POST",
    path: "/"
}

var request = http.request(option, function(resp) {
    resp.on("data", function(chunck) {
        console.log(chunck.toString());
    })
})
request.end();