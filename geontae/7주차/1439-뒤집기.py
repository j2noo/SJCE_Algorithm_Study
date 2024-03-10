s = input()
last = s[0]
cnt = 1
for i in range(1, len(s)):
    if s[i] != last:
        cnt += 1
        last = s[i]
print(cnt // 2)