const binaryInput = document.getElementById("binaryInput");
const decimalInput = document.getElementById("decimalInput");
const hexInput = document.getElementById("hexInput");

binaryInput.addEventListener("input", updateFromBinary);
decimalInput.addEventListener("input", updateFromDecimal);
hexInput.addEventListener("input", updateFromHex);

function updateFromBinary() {
    const binaryValue = binaryInput.value.trim();
    if (!/^[01]+$/.test(binaryValue)) return;

    const decimalValue = parseInt(binaryValue, 2);
    const hexValue = decimalValue.toString(16).toUpperCase();

    decimalInput.value = decimalValue;
    hexInput.value = hexValue;
}

function updateFromDecimal() {
    const decimalValue = parseInt(decimalInput.value);
    if (isNaN(decimalValue)) return;

    const binaryValue = decimalValue.toString(2);
    const hexValue = decimalValue.toString(16).toUpperCase();

    binaryInput.value = binaryValue;
    hexInput.value = hexValue;
}

function updateFromHex() {
    const hexValue = hexInput.value.trim().toUpperCase();
    if (!/^[0-9A-F]+$/.test(hexValue)) return;

    const decimalValue = parseInt(hexValue, 16);
    const binaryValue = decimalValue.toString(2);

    decimalInput.value = decimalValue;
    binaryInput.value = binaryValue;
}
