T = int(input())

for _ in range(T):
    whiteWrongPosCnt = 0
    blackWrongPosCnt = 0

    N = int(input())

    initState = input()
    targetState = input()

    for i in range(N):
        if initState[i] != targetState[i]:
            if initState[i] == 'W':
                whiteWrongPosCnt += 1
            else:
                blackWrongPosCnt += 1

    print(max(whiteWrongPosCnt, blackWrongPosCnt))

