def check(arr1, arr2):
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False

    return True

N = int(input())
arr = list(map(int, input().split(" ")))
rightPos = [False] * (N)

for i in range(len(arr)):
    if arr[i] == i + 1:
        rightPos[i] = True


