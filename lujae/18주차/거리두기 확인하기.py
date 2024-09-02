# 시간: 30분
# 풀이: BFS

import collections

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def is_range(y, x):
    return 0 <= y < 5 and 0 <= x < 5
def is_blocked(place, p1, p2, distance):
    dq = collections.deque()

    dq.append((p1[0], p1[1], 0))
    discovered = [[False] * 5 for i in range(5)]
    discovered[p1[0]][p1[1]] = True

    while dq:
        here = dq.popleft()

        for i in range(4):
            nextY = here[0] + dy[i]
            nextX = here[1] + dx[i]

            if is_range(nextY, nextX) and not discovered[nextY][nextX] and place[nextY][nextX] != 'X':
                if nextY == p2[0] and nextX == p2[1] and here[2] + 1 <= distance:
                    return False
                dq.append((nextY, nextX, here[2] + 1))
                discovered[nextY][nextX] = True

    return True



def get_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
def check(place):
    people_pos = []

    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                people_pos.append((i, j))

    no_distance_pair = []

    for i in range(len(people_pos)):
        for j in range(i + 1, len(people_pos)):
            d = get_distance(people_pos[i], people_pos[j])
            if d <= 2:
                no_distance_pair.append((people_pos[i], people_pos[j], d))

    for pair in no_distance_pair:
        if not is_blocked(place, pair[0], pair[1], pair[2]):
            return False

    return True

def solution(places):
    answer = []

    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)

    return answer