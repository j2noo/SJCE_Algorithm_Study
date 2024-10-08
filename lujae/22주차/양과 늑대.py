# 77.8점

import collections

SHIP = 0
WOLF = 1
def get_path(info, adj, here, visited, dic_path):
    visited |= 1 << here

    if info[here] == SHIP:
        dic_path[here] = visited

    for there in adj[here]:
        if visited & (1 << there) == 0:
            get_path(info, adj, there, visited, dic_path)
def get_cnt_in_visited(info, visited):
    ship_cnt = 0
    wolf_cnt = 0

    for i in range(len(info)):
        flag = info[i]

        pos_bit = 1 << i

        if flag == SHIP:
            if visited & pos_bit == pos_bit:
                ship_cnt += 1
        if flag == WOLF:
            if visited & pos_bit == pos_bit:
                wolf_cnt += 1

    return (ship_cnt, wolf_cnt)

def check(info, adj, visited, here, ship_cnt, wolf_cnt, end):
    visited.add(here)

    if info[here] == SHIP:
        ship_cnt += 1
    else:
        wolf_cnt += 1

    if ship_cnt <= wolf_cnt:
        return 0

    if here == end:
        return 1

    ret = 2
    for there in adj[here]:
        if there not in visited:
            tmp_ret = check(info, adj, visited, there, ship_cnt, wolf_cnt, end)
            if tmp_ret != 2:
                return tmp_ret

    return ret
def dp(info, adj, cache, dic_path, pos, visited):
    if cache[pos][visited] != -1:
        return cache[pos][visited]

    ret = 0

    for next_pos in dic_path[pos].keys():
        next_pos_bit = 1 << next_pos

        if pos == next_pos or (visited & next_pos_bit == next_pos_bit):
            continue

        next_path = dic_path[pos][next_pos]
        next_visited = visited | next_path

        (ship_cnt, wolf_cnt) = get_cnt_in_visited(info, visited)
        (next_ship_cnt, next_wolf_cnt) = get_cnt_in_visited(info, next_visited)

        if next_ship_cnt > next_wolf_cnt + 1:
            if check(info, adj, set(), pos, ship_cnt - 1, wolf_cnt, next_pos) != 2:
                ret = max(ret, next_ship_cnt - ship_cnt + dp(info, adj, cache, dic_path, next_pos, next_visited))

    cache[pos][visited] = ret
    return ret

def solution(info, edges):
    l = len(info)
    cache = [[-1] * (2 ** l) for _ in range(l)]

    adj = [[] for _ in range(len(info))]

    for edge in edges:
        u, v = edge
        adj[u].append(v)
        adj[v].append(u)

    dic_path = {}
    for i in range(len(info)):
        if info[i] == SHIP:
            tmp_path = {}
            get_path(info, adj, i, 0, tmp_path)
            dic_path[i] = tmp_path

    dp(info, adj, cache, dic_path, 0, 1)
    return cache[0][1] + 1
