# 최대공약수 구하기
def get_gcd(a, b):
  if (b == 0):
    return a;
  
  return get_gcd(b , a % b)

# 최소공배수 구하기
def get_lcm(a, b):
  return (a * b) / get_gcd(a, b)

# 답 알고리즘
# 1. N의 자리수들의 lcm(최소공배수) 구한다.
# 2. N으로 시작하는 숫자 뒤에 0~9, 0~99 이런식으로 범위를 넓혀가며 lcm으로 나누어 떨어지는 지 확인한다.
def sol(N):
  lcm = 1
  numeral = list(map(int, set(list(N))))
  
  for i in numeral:
    if(i == 0):
      continue
    lcm = get_lcm(lcm, i)
  
  max = 1

  if (int(N) % lcm == 0):
    return int(N)

  while(True):
    max = max * 10
    for num in range(max):
      new_num = (int(N) * max) + num
      if (new_num % lcm == 0):
        return new_num



N = input()

print(sol(N))