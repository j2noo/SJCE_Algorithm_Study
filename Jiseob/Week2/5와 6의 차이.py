A, B = input().split()

minA = A.replace('6', '5')
minB = B.replace('6', '5')
minimumSum = int(minA) + int(minB)

maxA = A.replace('5', '6')
maxB = B.replace('5', '6')
maximumSum = int(maxA) + int(maxB)

print(minimumSum, end=' ')
print(maximumSum)