finger = int(input())
cnt = int(input())
ans = -1
if finger == 1:
    ans = cnt * 8
elif finger == 5:
    ans = 4 + cnt * 8
else:
    if cnt % 2 == 0:  # 짝수
        ans = (8 * (cnt // 2)) + finger - 1
    else:  # 홀수
        ans = (8 * (cnt // 2)) + 9 - finger

print(ans)

# 카운트가 0 : finger-1
# 카운트가 1 : 5+(5-finger) 5
# 카운트가 2: 

# finger가 1or 5

# 핑거 5,카운트가 1, = 5
# 핑거 4,카운트가 1, = 5 // cnt3,13
# 핑거 3,카운트가 1, = 6 // cnt3,14
# 핑거 2,카운트가 1, = 7
# 핑거 1,카운트가 1, = 8

## 핑거 1,5
# 핑거 1, 카운트 1 : 8
# 핑거1, 카운트2 : 16

# 핑거5 카운트 1 : 12
# 5,2 : 20
