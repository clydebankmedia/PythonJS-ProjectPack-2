// countdown.js

function startTimer() {
  console.log("start timer!");
}

function stopTimer() {
  console.log("stop timer!");
}

function resetTimer() {
  console.log("reset timer!");
}

document.getElementById("start").addEventListener("click", startTimer);
document.getElementById("stop").addEventListener("click", stopTimer);
document.getElementById("reset").addEventListener("click", resetTimer);
