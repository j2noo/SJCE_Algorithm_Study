def change(str, ch1, ch2):
    tmp = str[:]
    return tmp.replace(ch1, ch2)

A, B = input().split()

minA = int(change(A, "6", "5"))
minB = int(change(B, "6", "5"))

maxA = int(change(A, "5", "6"))
maxB = int(change(B, "5", "6"))

print("%d %d" %(minA + minB, maxA + maxB))
