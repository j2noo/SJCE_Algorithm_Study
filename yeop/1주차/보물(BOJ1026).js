const fs = require('fs');
// const filePath = __dirname + '/1026.txt';
const filePath = '/dev/stdin';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const n = +input[0];
const A = input[1].split(' ').map((v) => +v);
const B = input[2].split(' ').map((v) => +v);

function getS(n, arr1, arr2) {
  let sum = 0;

  for (let i = 0; i < n; i++) {
    sum += arr1[i] * arr2[i];
  }

  return sum;
}

// [..., [숫자, 원래 자리 idx]] 숫자 기준 오름차순 정렬
let rankB = B.map((v, idx) => [v, idx]);
rankB = rankB.sort((a, b) => b[0] - a[0]);

// A를 오름차순으로 정렬 1 2 3 4 5
// B를 내림차순으로 정렬 5 4 3 2 1 (3 4 1 2 5)
let sortedA = A.sort((a, b) => a - b);

let newA = [];
rankB.forEach((v, idx) => (newA[v[1]] = sortedA[idx]));

console.log(getS(n, newA, B));
