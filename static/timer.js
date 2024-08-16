// this took me so long omg
let start = document.getElementById('start');
let stop = document.getElementById('stop');
let end = document.getElementById('end');

let hour = 0;
let minute = 0;
let second = 0;
let count = 0;
let timer = false;

start.addEventListener('click', function () { // Start timer when clicked, turn timer true
  timer = true;
  stopWatch();
});

stop.addEventListener('click', function () { // Stop timer when clicked, turn timer false
  timer = false;
});

end.addEventListener('click', function () { // Reset timer when clicked
    timer = false;
    hour = 0;
    minute = 0;
    second = 0;
    count = 0;
    document.getElementById('hr').innerHTML = "00";  // change the html back to 00
    document.getElementById('min').innerHTML = "00";
    document.getElementById('sec').innerHTML = "00";
    document.getElementById('count').innerHTML = "00";
});

function stopWatch() {
  if (timer) {    // if timer is true
      count++;

      if (count == 100) {
          second++;
          count = 0;
      }

      if (second == 60) {  // 60 sec = 1 min
          minute++;
          second = 0;
      }

      if (minute == 60) {  //60 min = 1 h
          hour++;
          minute = 0;
          second = 0;
      }

      let hrString = hour;  
      let minString = minute;
      let secString = second;
      let countString = count;

      if (hour < 10) {   // always display as double digit
          hrString = "0" + hrString;
      }

      if (minute < 10) {
          minString = "0" + minString;
      }

      if (second < 10) {
          secString = "0" + secString;
      }

      if (count < 10) {
          countString = "0" + countString;
      }

      //change the html to the new value
      document.getElementById('hr').innerHTML = hrString;  
      document.getElementById('min').innerHTML = minString;
      document.getElementById('sec').innerHTML = secString;
      setTimeout(stopWatch, 10); // 10ms delay
  }
}