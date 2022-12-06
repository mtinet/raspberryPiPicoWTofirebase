function setup() {
  createCanvas(400, 400);

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
  textSize(100);
  textAlign(CENTER);
  text("점수", width / 2, height / 2);
}
