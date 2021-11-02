var http = require('http');
var server = http.createServer(function(request, response) {

    response.writeHead(200, { "Content-Type": "text\plain" });
    if (request.method == "GET") {
        response.end("received GET request.")
    } else if (request.method == "POST") {
        response.end("received POST request.");
    } else {
        response.end("Undefined request .");
    }
});

server.listen(8000);
console.log("Server running on port 8000");