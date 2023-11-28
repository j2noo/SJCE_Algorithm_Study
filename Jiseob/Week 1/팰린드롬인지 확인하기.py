userInput = input()

if userInput[::1] == userInput[::-1]:
    print(1)
else:
    print(0)
