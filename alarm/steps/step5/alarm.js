// Set this to the snooze time you want, in milliseconds. For testing
// I keep it to small values, like 3 seconds.
SNOOZE_TIME = 3000;

let gTimeoutHandle, gSnoozeCount = 0;

alarmForm = document.forms['alarmForm']
alarmForm.addEventListener('submit', addAlarm);
  
function addAlarm(e) {
  e.preventDefault();
  const data = e.target.elements;
  const deadline = new Date(data.datetime.value);
  const name = data.name.value || "(unnamed)";
  gSnoozeCount = 0;

  // Add info to DOM.
  document.getElementById("activeAlarmName").textContent = name;

  // If you are not in the US and experience problems with
  // toLocaleString(), see
  // https://stackoverflow.com/questions/57666095/browser-default-locale-intl-datetimeformat-vs-navigator-language
  document.getElementById("activeAlarmTime").textContent = deadline.toLocaleString();
  document.getElementById("activeAlarmSnoozeCount").textContent = "";

  // Make it all visible.
  document.getElementById("alarmInfo").style.display = "block";

  const diff = deadline - new Date();
  gTimeoutHandle = setTimeout(() => activateAlarm(), diff);

  // Note that by resetting, you'll get an empty datetime element. In
  // step 6, this will be marked as invalid. To fix it, you'd need to
  // choose a reasonable default value and set it here. I'll leave
  // that to you.
  e.target.reset();
  
  data.datetime.disabled = true; // This version only supports one alarm at a time.
}
  
function activateAlarm() {
  document.getElementById("alarmIndicator").style.display = "block";
  document.getElementById("alarmSound").play();
}
  
// OPTIONAL: when testing it's annoying to have to enter datetimes
// manually. So this always sets the datetime to right now.
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

document.addEventListener("DOMContentLoaded", resetAlarmForm);

function cancelAlarm() {
  clearTimeout(gTimeoutHandle);
  document.getElementById("alarmInfo").style.display = "none";
  document.getElementById("alarmIndicator").style.display = "none";
  document.getElementById("alarmSound").pause();
  alarmForm.datetime.disabled = false;
}

document.getElementById("cancelBtn").addEventListener('click', cancelAlarm);
  
function snoozeAlarm() {
  clearTimeout(gTimeoutHandle);
  document.getElementById("alarmIndicator").style.display = "none";
  document.getElementById("alarmSound").pause();
  gTimeoutHandle = setTimeout(() => activateAlarm(), SNOOZE_TIME);
  gSnoozeCount++;
  document.getElementById("activeAlarmSnoozeCount").textContent = `(Snoozed ${gSnoozeCount} times)`;
}

document.getElementById("finishBtn").addEventListener('click', cancelAlarm);
document.getElementById("snoozeBtn").addEventListener('click', snoozeAlarm);
