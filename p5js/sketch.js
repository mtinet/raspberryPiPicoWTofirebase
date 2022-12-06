var nameInput;
var submitButton;
var database;
var button;
var score;

function setup() {
  createCanvas(400, 400);
  score = 0;
  createP('Click the button to get points');
  button = createButton('click');
  button.mousePressed(increaseScore);
  nameInput = createInput('name');
  submitButton = createButton('submit');
  submitButton.mousePressed(submitScore);
  
    // Initialize Firebase
  var config = {
    apiKey: "AIzaSyA4JNrHtS9pc6QaW8dtwATWhUhs0Ni8OBI",
    authDomain: "smartfarm-f867f.firebaseapp.com",
    databaseURL: "https://smartfarm-f867f-default-rtdb.firebaseio.com",
    projectId: "smartfarm-f867f",
    storageBucket: "",
    messagingSenderId: "605663694333"
}
  firebase.initializeApp(config); 
  database = firebase.database();
  
  var ref = database.ref('smartFarm');
  ref.on('value', gotData, errData);

}

function gotData (data) {
  	//console.log(data.val());
	var val = data.val();
    console.log(val);
  	var keys = Object.keys(val);
  	console.log(keys);
    var values = Object.values(val);
    console.log(values);
  
	for (var i = 0; i < keys.length; i++) {
	  var k = keys[i];
      console.log(k)
      var v = values[i];
      console.log(v);
      console.log(k + ":" + v)
	}
}

function errData(err) {
	console.log('Error!');
  	console.log(err);
}


function increaseScore() {
	score++;
}
function draw() { 
  background(200);
  textSize(100);
  textAlign(CENTER);
  text(score, width/2, height/2);
}


function submitScore() {
  	var data = {
  		name: nameInput.value(),
		score: score
  	}
  	var ref = database.ref('scores');
  	ref.push(data);
  	//console.log(data);
  	score = 0;
}
