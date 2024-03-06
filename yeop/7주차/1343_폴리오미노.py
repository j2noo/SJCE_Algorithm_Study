# 입력
string = input()
N = len(string)

# 메인 로직
answer = string.replace('XXXX', 'AAAA')
answer = answer.replace('XX', 'BB')

if 'X' in answer:
  answer = -1

print(answer)