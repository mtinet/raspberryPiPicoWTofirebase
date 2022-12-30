let humi = 0;
let temp = 0;
let light = 0;
let fanStatus = Boolean(false);
let ledStatus = Boolean(false);
let led;
let fan;
let button1;
let button2;
let minGyeong;

function preload() {
  led = loadImage('assets/led.png');
  fan = loadImage('assets/fan.png');
  minGyeong = loadFont('assets/NanumYeBbeunMinGyeongCe.ttf');
}

function setup() {
  createCanvas(windowWidth, windowHeight);
  textFont(minGyeong);
  
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

function draw() {
  background(200, 150, 100);
  
  fill(0);
  textSize(windowWidth/5);
  textAlign(CENTER);
  
  text("스마트 팜", width / 2, height * 1 / 6);
  textSize(windowWidth/8)
  text("습도 : " + humi, width / 2, height * 2 / 6);
  text("온도 : " + temp, width / 2, height * 3 / 6);
  text("조도 : " + light, width / 2, height * 4 / 6);
  
  if (ledStatus == 0) {
    fill(0, 0, 0);
    ellipse(width*2/10, height*8/10, windowWidth/10, windowWidth/10);
  } else {
    fill(255, 0, 0);
    ellipse(width*2/10, height*8/10, windowWidth/10, windowWidth/10);
  }
  
  if (fanStatus == 0) {
    fill(0, 0, 0);
    ellipse(width*6/10, height*8/10, windowWidth/10, windowWidth/10);
  } else {
    fill(255, 0, 0);
    ellipse(width*6/10, height*8/10, windowWidth/10, windowWidth/10);
  }
  
  // led 버튼
  button1 = createImg('assets/led.png');
  button1.position(width*2/10, height*8/10);
  button1.mousePressed(ledOnOff);
  
  if(mouseX > button1.x && mouseX < button1.x + button1.width && mouseY > button1.y && mouseY < button1.y + button1.height && mouseIsPressed === true && mouseButton === LEFT) {
      noTint();
      image(led, width*2.3/10, height*8/10);
    } else {
      
    }
  
  // fan 버튼
  button2 = createImg('assets/fan.png');
  button2.position(width*6/10, height*8/10);
  button2.mousePressed(fanOnOff);
  
    if(mouseX > button2.x && mouseX < button2.x + button2.width && mouseY > button2.y && mouseY < button2.y + button2.height && mouseIsPressed === true && mouseButton === LEFT) {
      tint(150, 210, 230);
      image(fan, width*6.3/10, height*8/10);
    } else {
      noTint();
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

function fanOnOff() {
  if (fanStatus == false) {
    fanStatus = true;
    
    var ref = database.ref('smartFarm');
    ref.update({
      fan: 1
    })
  } else {
    fanStatus = false;
    
    var ref = database.ref('smartFarm');
    ref.update({
      fan: 0
    })
  }
  //console.log(fanStatus);
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
  light = val.light;
  ledStatus = val.led;
  fanStatus = val.fan;
  //console.log(val.humi)
  //console.log(val.temp)
  //console.log(val.light)
  
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
