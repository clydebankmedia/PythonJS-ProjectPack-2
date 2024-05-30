const binaryInput = document.getElementById("binaryInput");
const decimalInput = document.getElementById("decimalInput");
const hexInput = document.getElementById("hexInput");

binaryInput.addEventListener("input", updateFromBinary);
decimalInput.addEventListener("input", updateFromDecimal);
hexInput.addEventListener("input", updateFromHex);

function updateFromBinary() {
  const number = parseInt(binaryInput.value.trim(), 2);
  decimalInput.value = number.toString(10);
  hexInput.value = number.toString(16).toUpperCase();
}

function updateFromDecimal() {
  const number = parseInt(decimalInput.value.trim(), 10);
  binaryInput.value = number.toString(2);
  hexInput.value = number.toString(16).toUpperCase();
}

function updateFromHex() {
  const number = parseInt(hexInput.value.trim().toUpperCase(), 16);
  decimalInput.value = number.toString(10);
  binaryInput.value = number.toString(2);
}
