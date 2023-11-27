str = input()

i = 0
j = len(str) - 1
result = 1
while 1:
    if (i >= j):
        break
    elif (str[i] != str[j]):
        result = 0
        break
    else:
        i += 1
        j -= 1

print(result)
