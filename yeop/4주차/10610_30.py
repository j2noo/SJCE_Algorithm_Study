N = list(input())

N.sort(reverse = True)

def sol():
  if '0' not in N:
    return -1
  total = sum(list(map(int, N)))

  if (total % 3 == 0):
    return int(''.join(N))
  else:
    return -1
  
print(sol())