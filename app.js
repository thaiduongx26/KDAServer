// Full Documentation - https://www.turbo360.co/docs
const vertex = require('vertex360')({site_id: process.env.TURBO_APP_ID})
const Chatroom = require('./models/Chatroom')
const bodyParser = require('body-parser')
const mongoose = require('mongoose')
// ObjectId = mongoose.Types.ObjectId
const config = {
	db: { 					// Database configuration. Remember to set env variables in .env file: MONGODB_URI, PROD_MONGODB_URI
		// url: (process.env.TURBO_ENV == 'dev') ? process.env.MONGODB_URI : process.env.PROD_MONGODB_URI,
		url: "mongodb://localhost/KDAServer",
		type: 'mongo',
		onError: (err) => {
			console.log('DB Connection Failed!')
		},
		onSuccess: () => {
			console.log('DB Successfully Connected!')
		}
	}
}
// console.log(ObjectId())
const app = vertex.app(config) // initialize app with config options
var http = require('http').createServer(app);
var io = require('socket.io').listen(http);

// import routes
const index = require('./routes/index')
const api = require('./routes/api')

app.get('/', function(req, res){
	res.sendFile('./public' + '/index.html');
});


// set routes
// app.use('/', index)
// support parsing of application/json type post data
app.use(bodyParser.json());

//support parsing of application/x-www-form-urlencoded post data
app.use(bodyParser.urlencoded({ extended: true }));
app.use('/api', api) // sample API Routes

// a = {_id: "5d07a7588d2b86775084ce86",
//     author1: "5d06094b046848a0fe30f474",
//     author2: "5d04abfda4b183c7cbe98292",
// 	date: "2019-06-17T14:44:40.683Z"
// }

// a.partner = 123
// console.log(a)



module.exports = app