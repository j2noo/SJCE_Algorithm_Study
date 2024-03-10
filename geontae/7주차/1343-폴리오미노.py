s = input()
res = ''
cnt = 0
s += '.'
for i in range(0, len(s)):
    if s[i] == 'X':
       cnt += 1
    else:
        if cnt % 4 == 0:
            res += 'A'*cnt
        elif cnt % 4 == 2:
            res += 'A'*(cnt-2) + 'BB'
        elif cnt % 2 == 0:
            res += 'BB'
        else:
            res = -1
            break
        cnt = 0
        res += '.'

if res != -1:
    print(res[0:len(s)-1])
else:
    print(res)