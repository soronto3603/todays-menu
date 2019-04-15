var express = require('express');
var app = express();
app.set('view engine','pug');
app.get('/', function (req, res) {
	res.render('index',{});
});

app.get('/save', function(req ,res){
  const fs = require('fs');
  
  const append_string=`${req.query.time},${req.query.emotion},${req.query.weather},${req.query.menu}\n`;
  
  var today = new Date();
  var dd = today.getDate();
  var mm = today.getMonth() + 1; //January is 0!

  var yyyy = today.getFullYear();
  if (dd < 10) {
    dd = '0' + dd;
  } 
  if (mm < 10) {
    mm = '0' + mm;
  } 
  var today = dd + mm + yyyy;
  
  fs.appendFile(`../dataset/${today}.csv`, append_string, (err)=>{
    if(err){
      return console.log(err)
    }
  })
  res.send("suc")
});
app.get('/weather', function (req, res) {
  // let lat=126.713513
  // let lon=35.947230
  
  // const https=require('https')
  // const options={
  //   hostname:'samples.openweathermap.org',
  //   port:'80',
  //   path:`/data/2.5/weather?lat=${lat}&lon=${lon}`,
  //   method:'GET'
  // }
  // https.request(options,(r)=>{
  //   res.send(r)
  // })


  res.send("hi")
});

app.listen(3000, function () {
  console.log('우리가 어떤 민족 입니까.');
});

app.use(express.static('public'));