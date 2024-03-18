S1 = input()

cnt1 = 0
cnt2 = 0

for s in S1.split('1'):
    if s != '':
        cnt1 += 1
for s in S1.split('0'):
    if s != '':
        cnt2 += 1

print(min(cnt1, cnt2))
