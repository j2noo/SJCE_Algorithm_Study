S = list(map(int, list(input()))) # len(S) <= 1_000_000

count_one_seq = 0 # 연속된 1로 이루어진 문자열의 수
count_zero_seq = 0 # 연속된 0으로 이루어진 문자열의 수

# 첫 번째 글자 조사
if (S[0] == 0):
  count_zero_seq += 1
else:
  count_one_seq += 1

# 나머지 글자 조사
for i in range(1, len(S)):
  # prev - curr == 1 -> count_one_seq++
  if (S[i] - S[i-1] == 1):
    count_one_seq += 1
    
  # prev - curr == -1 -> count_zero_seq++
  elif (S[i] - S[i-1] == -1):
    count_zero_seq += 1
    
  # prev - curr == 0 -> continue
  else:
    continue

# 답
print(min(count_one_seq, count_zero_seq))