let button;
let humi = 0;
let temp = 0;
let ledStatus = Boolean(false);

function setup() {
  createCanvas(windowWidth, windowHeight);
  background(200);
  
  button = createButton('LED 제어');
  button.size(100,80);
  button.position(width*8/10, height*9/10);
  button.mousePressed(ledOnOff);

  // Initialize Firebase
  var config = {
    apiKey: "AIzaSyA4JNrHtS9pc6QaW8dtwATWhUhs0Ni8OBI",
    authDomain: "smartfarm-f867f.firebaseapp.com",
    databaseURL: "https://smartfarm-f867f-default-rtdb.firebaseio.com",
    projectId: "smartfarm-f867f",
    storageBucket: "",
    messagingSenderId: "605663694333",
  };
  firebase.initializeApp(config);
  database = firebase.database();

  var ref = database.ref("smartFarm");
  ref.on("value", gotData, errData);
}

function gotData(data) {
  //console.log(data.val());
  var val = data.val();
  //console.log(val);
  var keys = Object.keys(val);
  //console.log(keys);
  var values = Object.values(val);
  //console.log(values);
  
  humi = val.humi;
  temp = val.temp;
  ledStatus = val.led;
  //console.log(val.humi)
  //console.log(val.temp)

  for (var i = 0; i < keys.length; i++) {
    var k = keys[i];
    //console.log(k)
    var v = values[i];
    //console.log(v);
    console.log(k + ":" + v);
  }
}

function errData(err) {
  console.log("Error!");
  console.log(err);
}

function draw() {
  background(200);
  fill(0);
  textSize(windowWidth/5);
  textAlign(CENTER);
  
  text("습도 : " + humi, width / 2, height * 1 / 4);
  text("온도 : " + temp, width / 2, height * 2 / 4);
  
  if (ledStatus == 0) {
    fill(0, 0, 0);
    ellipse(width/2, height * 3.5 / 5, windowWidth/5, windowWidth/5);
  } else {
    fill(255, 0, 0);
    ellipse(width/2, height * 3.5 / 5, windowWidth/5, windowWidth/5);
  }
}

function ledOnOff() {
  if (ledStatus == false) {
    ledStatus = true;
    
    var ref = database.ref('smartFarm');
    ref.update({
      led: 1
    })
  } else {
    ledStatus = false;
    
    var ref = database.ref('smartFarm');
    ref.update({
      led: 0
    })
  }
  //console.log(ledStatus);
}
