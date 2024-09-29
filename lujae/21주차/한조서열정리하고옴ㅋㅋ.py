N = int(input())
heights = list(map(int, input().split(" ")))

ret = 0
current_height = heights[0]
cnt_kill = 0

for i in range(1, len(heights)):
    if current_height < heights[i]:
        ret = max(ret, cnt_kill)
        current_height = heights[i]
        cnt_kill = 0
    else:
        cnt_kill += 1

ret = max(ret, cnt_kill)
print(ret)