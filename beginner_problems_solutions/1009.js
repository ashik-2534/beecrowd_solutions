var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var sellerName = lines[0];
var salary = parseFloat(lines[1]);
var sales = parseFloat(lines[2]);

var totalSalary = salary + (sales * 0.15);

console.log("TOTAL = R$ " + totalSalary.toFixed(2));