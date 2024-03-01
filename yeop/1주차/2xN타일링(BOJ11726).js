const fs = require('fs');
// const filepath = __dirname + '/11726.txt';
const filepath = '/dev/stdin';
const input = fs.readFileSync(filepath).toString().trim();

const n = BigInt(input);

// 9 = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 -> 9!/9! -> 9C0 = 1
//   = 2 + 1 + 1 + 1 + 1 + 1 + 1 + 1 -> 8!/1!7! -> 8C1 = 8
//   = 2 + 2 + 1 + 1 + 1 + 1 + 1 -> 7!/2!5! -> 7C2 = 21
//   = 2 + 2 + 2 + 1 + 1 + 1 -> 6!/3!3! -> 6C3 = 20
//   = 2 + 2 + 2 + 2 + 1 -> 5!/4!1! -> 5C4 = 5

// 조합 합으로 풀려다가 걍 분할통치로 품

function solution(n) {
  if (n === 1n) return 1n;
  if (n === 2n) return 2n;
  if (n === 3n) return 3n;

  const a = n / 2n;
  const b = n - a;

  return solution(a) * solution(b) + solution(a - 1n) * solution(b - 1n);
}

console.log(Number(solution(n) % 10007n));
