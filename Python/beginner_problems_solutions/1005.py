var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var A = parseFloat(lines[0]);
var B = parseFloat(lines[1]);

var average = (A*3.5 + B*7.5) / (3.5 + 7.5);

console.log("MEDIA = " + average.toFixed(5));
