var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var code1 = parseInt(lines[0].split(' ')[0]);
var quantity1 = parseInt(lines[0].split(' ')[1]);
var price1 = parseFloat(lines[0].split(' ')[2]);

var code2 = parseInt(lines[1].split(' ')[0]);
var quantity2 = parseInt(lines[1].split(' ')[1]);
var price2 = parseFloat(lines[1].split(' ')[2]);

var total = (quantity1 * price1) + (quantity2 * price2);

console.log("VALOR A PAGAR: R$ " + total.toFixed(2));