const fs = require('fs');
// const filepath = __dirname + '/2667.txt';
const filepath = '/dev/stdin';
const input = fs.readFileSync(filepath).toString().trim().split('\n');

// 입력
const n = input[0]; // 정사각형 크기
const arr = input // 단지 배열
  .slice(1)
  .map((v) => v.split(''))
  .map((row) => row.map((v) => ({ num: +v, marked: false })));

/**
 * 해당 집이 포함된 단지 수 구하기
 * @param {number} y - 배열 y좌표
 * @param {number} x - 배열 x좌표
 * @returns 마킹이거나 집이 아니면 0 반환, 노마킹에 집이면 1 + 상하좌우 재귀 결과값
 */
function getCount(y, x) {
  // 인덱스 조건
  if (y < 0 || y >= n || x < 0 || x >= n) return 0;

  // 집이 없거나 마킹되어있으면 0 반환
  if (arr[y][x].num === 0 || arr[y][x].marked) return 0;

  if (arr[y][x].num === 1) {
    arr[y][x].marked = true;

    return (
      1 +
      getCount(y, x - 1) +
      getCount(y, x + 1) +
      getCount(y - 1, x) +
      getCount(y + 1, x)
    );
  }
}

let total = [];

// 배열 돌아서 마킹 안되어있거나 1이면 getCount 호출해서 단지 수 배열에 push
for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (!arr[i][j].marked && arr[i][j].num === 1) {
      total.push(getCount(i, j));
    }
  }
}

console.log(total.length); // 총 단지 수 출력

// 단지 수 오름차순 정렬 후 출력
total
  .sort((a, b) => a - b)
  .forEach((v) => {
    console.log(v);
  });
