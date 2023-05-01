
const fs = require('fs');
const tmi = require('tmi.js');
var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var path = require('path');
// const cors = require('cors');
// let corsOptions = {
//     origin: 'localhost',
//     credentials: true
// }

//temp log folder - chat message 
folder = path.resolve(__dirname) + '\\log\\';

// tmi.js load
const client = new tmi.Client({
    channels: ['32comma'] //<-- channel name
});

//channel connect
client.connect();
http.listen(8080, function () {
    console.log('Socket IO server listening on port 8080');
});
console.log('Server is running ');

io.on('connection', function (client) {
    client.on('message', function (msg) {
        io.sockets.send(msg);
        console.log(msg);
    });
    client.on('disconnect', function (e) {
        console.log(e);
    });
});
app.get('/', function (req, res) {
    res.sendFile(__dirname + "/index.html")
})
client.on('message', (channel, tags, message, self) => {
    //let content = `${tags['display-name']}: ${message}\n`;


    // set chat message log folder -- timestamp save
    fs.writeFile(folder + `${new Date().getTime()}.txt`,
        message, { flag: 'a+' }, err => { });
    console.log(message);

    io.sockets.send(message);
});

