const SNOOZE_TIME = 3000;
let gTimeoutHandle, gSnoozeCount = 0;

// Note: This is really just for ease of testing. The main problem is
// that validity is only checked when the input is /changed/ (by the
// user), so by setting it this way, you can create an alarm that will
// go off immediately. But that's exactly what I want for testing.
function resetAlarmForm() {
  const now = new Date();
  const year = now.getFullYear();
  const month = (now.getMonth() + 1).toString().padStart(2, "0");
  const day = now.getDate().toString().padStart(2, "0");
  const hours = now.getHours().toString().padStart(2, "0");
  const minutes = now.getMinutes().toString().padStart(2, "0");

  const dateStr = `${year}-${month}-${day}`;
  const timeStr = `${hours}:${minutes}`;

  document.forms['alarmForm'].elements.datetime.value = `${dateStr}T${timeStr}`;
}

function checkAlarmValidity(e) {
  const deadline = new Date(e.target.value);
  const now = new Date();
  if (deadline <= now) {
    e.target.setCustomValidity("Please enter a future date and time.");
  } else {
    e.target.setCustomValidity(""); // must clear it, otherwise it will keep the error message
  }
  e.target.reportValidity();
}

function addAlarm(e) {
  e.preventDefault();
  const data = e.target.elements;
  const deadline = new Date(data.datetime.value);
  const name = data.name.value || "(unnamed)";
  gSnoozeCount = 0;

  // Add info to DOM.
  document.getElementById("activeAlarmName").textContent = name;
  document.getElementById("activeAlarmTime").textContent = deadline.toLocaleString();
  document.getElementById("activeAlarmSnoozeCount").textContent = "";
  document.getElementById("alarmInfo").style.display = "block";

  const diff = deadline - new Date();
  gTimeoutHandle = setTimeout(() => activateAlarm(), diff);

  e.target.reset();
  resetAlarmForm();
}

function cancelAlarm() {
  clearTimeout(gTimeoutHandle);
  document.getElementById("alarmInfo").style.display = "none";
  document.getElementById("alarmIndicator").style.display = "none";
  document.getElementById("alarmSound").pause();
}

function snoozeAlarm() {
  clearTimeout(gTimeoutHandle);
  document.getElementById("alarmIndicator").style.display = "none";
  document.getElementById("alarmSound").pause();
  gTimeoutHandle = setTimeout(() => activateAlarm(), SNOOZE_TIME);
  gSnoozeCount++;
  document.getElementById("activeAlarmSnoozeCount").textContent = `(Snoozed ${gSnoozeCount} times)`;
}

function activateAlarm() {
  document.getElementById("alarmIndicator").style.display = "block";
  document.getElementById("alarmSound").play();
}

document.addEventListener("DOMContentLoaded", resetAlarmForm);
alarmForm = document.forms['alarmForm']
alarmForm.addEventListener('submit', addAlarm);
alarmForm.addEventListener('change', checkAlarmValidity);

document.getElementById("cancelBtn").addEventListener('click', cancelAlarm);
