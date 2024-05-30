const UPDATE_INTERVAL = 1000;
let gDeadline; // active countdown deadline
let gIntervalId; // handle saved here to clear later

function updateTimer() {
  const now = new Date();
  const diff = now - gDeadline;
  console.log(diff);
}
  
function startTimer() {
  clearInterval(gIntervalId);

  // clear any styling that may be set when a timer expires
  document.getElementById("countdown").style.color = "black";
  document.getElementById("countdown").classList = [];
  
  // Careful: passing a date string to the Date constructor will interpret it
  // as UTC instead of local timezone.
  const parts = document.getElementById("date").value.split("-")

  // Map is kind of like a for loop: iterate over every element of
  // parts, converting each to an integer. Returns an array with the
  // results.
  const [year, month, day] = parts.map(x => parseInt(x));
  
  const time = document.getElementById("time").value;
  const [hours, minutes] = time.split(":");

  // `month - 1` since Date uses zero-indexed months
  gDeadline = new Date(year, month - 1, day, hours, minutes);
  
  gIntervalId = setInterval(updateTimer, UPDATE_INTERVAL);
}
  
function stopTimer() {
    clearInterval(gIntervalId);
}
  
function resetTimer() {
  console.log("reset timer!");
}

document.getElementById("start").addEventListener("click", startTimer);
document.getElementById("stop").addEventListener("click", stopTimer);
document.getElementById("reset").addEventListener("click", resetTimer);
