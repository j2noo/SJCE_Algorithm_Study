dx = [0, 1, 0, 1]
dy = [0, 0, 1, 1]



def quadTree(arr, posX, posY, size):
  if (size == 1):
    return int(arr[posY][posX])

  tree = []
  half = int(size / 2)
  for i in range(4):
    x = dx[i] * half
    y = dy[i] * half
    
    tree.append(quadTree(arr, posX + x, posY + y, half))
    
  if (tree[0] == tree[1] == tree[2] == tree[3] and tree[0] in [0, 1]):
    return tree[0]
  
  return "(%s%s%s%s)" %(tree[0], tree[1], tree[2], tree[3])

# 입력
n = int(input())
video = list(input() for _ in range(n))

print(quadTree(video, 0, 0, n))