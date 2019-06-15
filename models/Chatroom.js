const mongoose = require('mongoose')
const Chat = require("../models/Chat")
var ObjectId = mongoose.Schema.Types.ObjectId;

const Chatroom = new mongoose.Schema({
    author1: ObjectId,
    author2: ObjectId,
    date: Date,
    lastMessage: Date,
    chat: [Chat]
})

module.exports = mongoose.model('Chatroom', Chatroom)