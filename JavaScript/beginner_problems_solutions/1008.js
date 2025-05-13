var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var employeeNumber = parseInt(lines.shift());
var workedHours = parseInt(lines.shift());
var hourlyWage = parseFloat(lines.shift());

var salary = workedHours * hourlyWage;

console.log("NUMBER = " + employeeNumber);
console.log("SALARY = U$ " + salary.toFixed(2));