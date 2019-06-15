// Full Documentation - https://www.turbo360.co/docs
const turbo = require('turbo360')({site_id: process.env.TURBO_APP_ID})
const vertex = require('vertex360')({site_id: process.env.TURBO_APP_ID})
const router = vertex.router()
const Chatroom = require('../models/Chatroom')
/*  This is a sample API route. */

router.get('/getChatroom/:userid', (req, res) => {
	auth = req.params.userid
	// console.log(req.params.id)
	Chatroom.find({
		$or: [{author1: auth}, {author2: auth}]
	}).sort({lastMessage: -1}).exec(function(err, result){
		res.json(result)
	})
})

router.post('/createRoom', (req, res) => {
	auth1 = req.body.auth1
	auth2 = req.body.auth2
	Chatroom.findOne({
		$or: [{author1: auth1, author2: auth2}, {author1: auth2, author2: auth1}]
	}).exec(function (err, results) {
		if(err){
			console.log(err)
		}
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
		} else {
			res.json({
				code: 400,
				roomId: results._id.toString(),
				message: "Room da ton tai"
			})
		}
	});
	
})



module.exports = router
