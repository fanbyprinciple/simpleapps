const token = require('./token.js')
console.log('nyahcat I am! ' + token.token)
const Discord = require('discord.js')
const client = new Discord.Client()

client.login(token.token)

client.on('ready', readyDiscord )

function readyDiscord(){
    console.log('I am ready!')
}

client.on('message', gotMessage)

function gotMessage(msg){
    console.log(msg.content)

    const replies = [
        'hi achu',
        'achoooo',
        'pika pika',
        'popopopolio',
        'kuchu',
        'chu*'
    ]

    if (msg.channel.id == '776104493648838678'){
        if (msg.content === 'chuchu'){
            // msg.reply('pikachu!')
            const r = Math.floor(Math.random() * replies.length)
            msg.channel.send(replies[r])
        }
    }
    
}