const fs = require('fs');

// Read input from a file
const input = fs.readFileSync('/dev/stdin', 'utf8');
const radius = parseFloat(input.trim());

// Function to calculate the volume of a sphere
function calculateVolume(radius) {
    const pi = 3.14159;
    const volume = (4.0 / 3) * pi * Math.pow(radius, 3);
    return volume;
}

// Calculate the volume
const volume = calculateVolume(radius);

// Output the volume with 3 decimal places
console.log(`VOLUME = ${volume.toFixed(3)}`);