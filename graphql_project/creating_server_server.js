var express = require('express')
var { graphqlHTTP } = require('express-graphql')
var { buildSchema } = require('graphql')

var schema = buildSchema(`
    type Query {
        hello: String
    }
`)

var root = {
    hello: ()=>{
        return 'Hello world!';
    },
}

var app = express()
app.use('/graphql', graphqlHTTP({
    schema: schema,
    rootValue:root,
    graphiql: true,
}))

app.listen(4000)
console.log('Running a GraphQL API server at http://loclahost:4000/graphql')
