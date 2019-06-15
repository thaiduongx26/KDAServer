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
  socket.on('newMessage', function(roomId, message){
    // message : {type, detail, auth}
    Chatroom.findOne({
      _id: roomId
    }).exec(function(err, res) {
      console.log(res)
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
      socket.emit('addMessage', roomId, newMess)
    })
  })
})

http.listen(5000, function(){
  console.log('listening on *:5000');
});