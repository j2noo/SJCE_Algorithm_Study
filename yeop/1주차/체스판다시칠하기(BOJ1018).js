const fs = require('fs');
// const filePath = '/dev/stdin';
const filePath = './1018.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');
const [n, m] = input[0].split(' ');
const chess = input.slice(1);

// M X N 보드
// 검은색 or 흰색
// 잘라서 8 x 8
// 검은색 흰색 번갈아서
const X = [
  'WBWBWBWB',
  'BWBWBWBW',
  'WBWBWBWB',
  'BWBWBWBW',
  'WBWBWBWB',
  'BWBWBWBW',
  'WBWBWBWB',
  'BWBWBWBW',
];

const Y = [
  'BWBWBWBW',
  'WBWBWBWB',
  'BWBWBWBW',
  'WBWBWBWB',
  'BWBWBWBW',
  'WBWBWBWB',
  'BWBWBWBW',
  'WBWBWBWB',
];

// str1과 str2는 각 8자리 문자열
function diffCountOneRow(str1, str2) {
  let count = 0;

  for (let i = 0; i < 8; i++) {
    if (str1[i] !== str2[i]) count++;
  }

  return count;
}

// arr1과 arr2의 각 원소는 는 모두 8글자 문자열, 각 배열의 길이도 8
function diffCountAllRow(arr1, arr2) {
  let count = 0;

  for (let i = 0; i < 8; i++) {
    count += diffCountOneRow(arr1[i], arr2[i]);
  }

  return count;
}

function getMin(a, b) {
  return a < b ? a : b;
}

let min = 64;

let row = 0;
let column = 0;

while (column <= m - 8) {
  const arr = chess.slice(row, row + 8).map((v) => v.slice(column, column + 8));

  min = getMin(min, getMin(diffCountAllRow(arr, X), diffCountAllRow(arr, Y)));

  row++;
  if (row > n - 8) {
    row = 0;
    column++;
  }
}

console.log(min);
