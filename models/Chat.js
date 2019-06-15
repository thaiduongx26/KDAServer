const mongoose = require('mongoose')

var ObjectId = mongoose.Schema.Types.ObjectId;

const Chat = new mongoose.Schema({
    _id: ObjectId,
    createdAt: Date,
    detail: String,
    type: String,
    seen: Boolean,
    auth: ObjectId
})

module.exports = Chat