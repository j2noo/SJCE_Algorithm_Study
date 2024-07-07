N = int(input())
S = input()

sp = S.split(")(")
cnt = 0

print(sp)
colsed = False
stOpen = []
stClosed = []
ret = 0

for ch in S:
    if ch == '(':
        stOpen.append(ch)
    else:

        stClosed.append(ch)


