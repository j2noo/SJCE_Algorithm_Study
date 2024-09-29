# 16분
N = int(input())
height_li = list(map(int,input().split()))

sort_li = []
for idx, h in enumerate(height_li):
    sort_li.append((h,idx))
    
sort_li.sort(reverse=True)


# 나보다 큰 봉우리중에 가장 왼쪽에 있는 봉우리
left_bong = N
ans = -1
for h, idx in sort_li:
    ans = max(ans, left_bong - idx - 1)
    left_bong = min(left_bong, idx)
    
print(ans)
# 정렬 후 큰 수부터 인덱스 차지