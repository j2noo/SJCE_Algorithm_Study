const fs = require('fs');
// const filePath = './10988.txt';
const filePath = '/dev/stdin';
const input = fs.readFileSync(filePath).toString().trim();

let flag = 1;

for (let i = 0, j = input.length - 1; i < j; i++, j--) {
  if (input[i] !== input[j]) {
    flag = 0;
    break;
  }
}

console.log(flag);
