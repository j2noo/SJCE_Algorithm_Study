from collections import deque

def solution(maps):
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # 문자열에서 정수로 변환한 새로운 2차원 리스트 생성
    new_maps = []
    for row in maps:
        new_row = []
        for cell in row:
            if cell == 'X':
                new_row.append(0)
            else:
                new_row.append(int(cell))
        new_maps.append(new_row)
        
    #bfs  
    for i in range(len(new_maps)):
        for j in range(len(new_maps[0])):
            if not visited[i][j] and new_maps[i][j]:
                queue = deque([(i, j)])
                cnt = new_maps[i][j]
                visited[i][j] = True

                while queue:
                    x, y = queue.popleft()

                    for d in range(4):
                        nx, ny = x + move[d][0], y + move[d][1]
                        if 0 <= nx < len(new_maps) and 0 <= ny < len(new_maps[0]) and new_maps[nx][ny] and not visited[nx][ny]:
                            queue.append((nx, ny))
                            cnt += new_maps[nx][ny]
                            visited[nx][ny] = True

                answer.append(cnt)

    if not answer:  # answer가 비어있다면
        return [-1]               
    
    answer.sort()
    return answer
