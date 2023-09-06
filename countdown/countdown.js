const updateInterval = 1000;
let deadline; // active countdown deadline
let intervalId; // handle saved here to clear later

const SECS_PER_HOUR = 60 * 60;
const SECS_PER_DAY = 24 * SECS_PER_HOUR;
const SECS_PER_MONTH = 30 * SECS_PER_DAY;
const SECS_PER_YEAR = 365 * SECS_PER_DAY;

function display(diff) {
    diff = Math.floor(diff / 1000); // convert from milliseconds to seconds
    const years = Math.floor(diff / SECS_PER_YEAR);
    diff -= years * SECS_PER_YEAR;
    const months = Math.floor(diff / SECS_PER_MONTH);
    diff -= months * SECS_PER_MONTH;
    const days = Math.floor(diff / SECS_PER_DAY);
    diff -= days * SECS_PER_DAY;
    const hours = Math.floor(diff / SECS_PER_HOUR);
    diff -= hours * SECS_PER_HOUR;
    const minutes = Math.floor(diff / 60);
    diff -= minutes * 60;
    const seconds = diff;

    document.getElementById("years").innerHTML = `${years} year` + (years > 1 ? "s" : "");
    document.getElementById("months").innerHTML = `${months} month` + (months > 1 ? "s" : "");
    document.getElementById("days").innerHTML = `${days} days` + (days > 1 ? "s" : "");
    document.getElementById("hours").innerHTML = `${hours}`.padStart(2, "0") + ':';
    document.getElementById("minutes").innerHTML = `${minutes}`.padStart(2, "0") + ':';
    document.getElementById("seconds").innerHTML = `${seconds}`.padStart(2, "0");

    if (years > 0) {
        document.getElementById("years").style.display = "inline";
    } else {
        document.getElementById("years").style.display = "none";
    }

    if (months > 0 || years > 0) {
        document.getElementById("months").style.display = "inline";
    } else {
        document.getElementById("months").style.display = "none";
    }

    if (days > 0 || months > 0 || years > 0) {
        document.getElementById("days").style.display = "inline";
    } else {
        document.getElementById("days").style.display = "none";
    }

    // always display these
    for (const id of ["hours", "minutes", "seconds"]) {
        document.getElementById(id).style.display = "inline";
    }
}

function updateTimer() {
    const now = new Date();
    if (!deadline) {
        resetTimer();
        return;
    }
    if (deadline < now) {
        stopTimer();
        display(0);
        document.getElementById("countdown").style.color = "red";
        document.getElementById("countdown").classList.add("blink");
    } else {
        display(deadline - now);
    }
}

function startTimer() {
    clearInterval(intervalId);
	  document.getElementById("countdown").style.color = "black";
    document.getElementById("countdown").classList = [];
	
    // Careful: passing a date string to the Date constructor will interpret it
    // as UTC instead of local timezone.
    const [year, month, day] = document.getElementById("date").value.split("-").map(x => parseInt(x));
    const time = document.getElementById("time").value;
    const [hours, minutes] = time.split(":");
    deadline = new Date(year, month - 1, day, hours, minutes);
    intervalId = setInterval(updateTimer, updateInterval);
}

function stopTimer() {
    clearInterval(intervalId);
}

function resetTimer() {
    stopTimer();
    for (id of ["years", "months", "days", "hours", "minutes", "seconds"]) {
        document.getElementById(id).style.display = "none";
    }
}

document.getElementById("start").addEventListener("click", startTimer);
document.getElementById("stop").addEventListener("click", stopTimer);
document.getElementById("reset").addEventListener("click", resetTimer);
