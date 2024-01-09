str = input()
newStr = ""
for idx in range(len(str) - 1, -1, -1):
    newStr += str[idx]
    
if newStr == str:
    print(1)
else:
    print(0)
