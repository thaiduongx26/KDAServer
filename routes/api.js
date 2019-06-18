// Full Documentation - https://www.turbo360.co/docs
const turbo = require('turbo360')({site_id: process.env.TURBO_APP_ID})
const vertex = require('vertex360')({site_id: process.env.TURBO_APP_ID})
const router = vertex.router()
const Chatroom = require('../models/Chatroom')
const https = require('https')
const request = require('request')
/*  This is a sample API route. */

function doRequest(url) {
	return new Promise(function (resolve, reject) {
		request(url, function (error, res, body) {
			if (!error) {
				resolve(body);
			} else {
				reject(error);
			}
		});
	});
  }

router.get('/getChatroom/:userid', async function(req, res) {
	auth = req.params.userid
	// console.log(req.params.id)
	let result = await  Chatroom.find({
		$or: [{author1: auth}, {author2: auth}]
	}).sort({lastMessage: -1}).then(response => {
		return response;
	});
	let data = []
	// var i = 0
	for(i = 0; i < result.length; i++) {
		let value = result[i]
		let a = {}
		let auth2 = ''
		if(auth == value['author1']){
			auth2 = value['author2']
		} else {
			auth2 = value['author1']
		}
		console.log(value) 
		let res = await doRequest('https://df4fb1f7.ngrok.io/user/' + auth2);
		a.partner = JSON.parse(res)
		a.room = {}
		a.room._id = value._id
		a.room.author1 = value.author1
		a.room.author2 = value.author2
		a.room.lastMessage = value.chat[value.chat.length-1]
		console.log(value) 
		// if (i == 1){
		// 	console.log(data)
		// }
		// console.log(a)
		data.push(a)
	}
	console.log(data)
	res.json(data)
})

router.get('/getChat/:roomId', async function(req, res) {
	roomId = req.params.roomId
	// console.log(req.params.id)
	let result = await  Chatroom.findOne({
		_id: roomId 
	}).then(response => {
		return response;
	});
	console.log(result)
	let data = {}
	// var i = 0
	data.code = 200
	data.message = "success"
	data.chat = result.chat
	// console.log(data)
	res.json(data)
})

router.post('/createRoom', (req, res) => {
	auth1 = req.body.auth1
	auth2 = req.body.auth2
	Chatroom.find({
		$or: [{author1: auth1, author2: auth2}, {author1: auth2, author2: auth1}]
	}).exec(function (err, results) {
		if(err){
			console.log(err)
		}
		console.log("res: "+ results)
		if(results.length == 0){
			data = {
				author1: auth1,
				author2: auth2,
				date: Date.now()
			} 
			const chatroom = new Chatroom(data)
			chatroom.save(function(err){
				if(err){
					console.log("create room error: " + err)
				}
			})
			res.json({
				code: 200,
				idRoom: chatroom._id.toString()
			})
		} else if(results.length == 1) {
			res.json({
				code: 400,
				roomId: results[0]._id.toString(),
				message: "Room da ton tai"
			})
		}
	});
	
})



module.exports = router
