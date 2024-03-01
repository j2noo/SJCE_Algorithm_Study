def isSquare(num):
  return int(num ** 0.5) ** 2 == num

def sol(m, n):
  ret = []
  
  for i in range(m, n + 1):
    if isSquare(i):
      ret.append(i)
      
  return ret
    
m = int(input())
n = int(input())

list = sol(m, n)
sumList = sum(list)

if(sumList):
  print(sumList)
  print(list[0])
else:
  print(-1)
  