var app = require('express')();
var http = require('http').createServer(app);
var io = require('socket.io')(http);

var mongoose = require('mongoose');
 
mongoose.connect('mongodb://localhost/KDAServer');
var ObjectId = mongoose.Types.ObjectId;
const Chatroom = require('./models/Chatroom')
const Chat = require('./models/Chat')

app.get('/', function(req, res){
  res.sendFile(__dirname + '/public/index.html');
});

io.of('chatroom').on('connection', function(socket){
  socket.on('newMessage', function(message){
    // message : {type, detail, auth}
    console.log(message)
    Chatroom.findOne({
      _id: message.roomId
    }).exec(function(err, res) {
      // console.log()
      ti = Date.now()
      chatroom = res
      newMess = {
        _id: ObjectId(),
        createdAt: ti,
        detail: message.detail,
        type: message.type,
        seen: false,
        auth: message.auth
      }
      chatroom.chat.push(newMess)
      chatroom.lastMessage = ti
      // console.log(res)
      chatroom.save(function(err){
        if(err){
          console.log("save chatroom error:  " + err)
        }
      })
      newMess.roomId = message.roomId
      socket.emit('addMessage', newMess)
    })
  })
})

http.listen(5000, function(){
  console.log('listening on *:5000');
});