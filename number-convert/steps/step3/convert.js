const binaryInput = document.getElementById("binaryInput");
const decimalInput = document.getElementById("decimalInput");
const hexInput = document.getElementById("hexInput");

binaryInput.addEventListener("input", updateFromBinary);
decimalInput.addEventListener("input", updateFromDecimal);
hexInput.addEventListener("input", updateFromHex);

function updateFromBinary() {
  const binaryStr = binaryInput.value.trim();
  if (!/^[01]+$/.test(binaryStr)) return;
  const number = parseInt(binaryStr, 2);
  decimalInput.value = number.toString(10);
  hexInput.value = number.toString(16).toUpperCase();
}

function updateFromDecimal() {
  const decimalStr = decimalInput.value.trim();
  if (!/^[0-9]+$/.test(decimalStr)) return;
  const number = parseInt(decimalStr, 10);
  binaryInput.value = number.toString(2);
  hexInput.value = number.toString(16).toUpperCase();
}

function updateFromHex() {
  const hexStr = hexInput.value.trim().toUpperCase();
  if (!/^[0-9A-F]+$/.test(hexStr)) return;
  const number = parseInt(hexStr, 16);
  decimalInput.value = number.toString(10);
  binaryInput.value = number.toString(2);
}
