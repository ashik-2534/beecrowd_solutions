var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var n = 3.14159;
var R = parseFloat(lines[0]);

var Area = n * (R * R);

console.log("A=" + Area.toFixed(4));