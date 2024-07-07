def solution(n, m, section):
    answer = 0
    while section:
        if len(section) > 0:
            next_pos = section[0] + m
            while section and section[0] < next_pos:
                section.pop(0) # O(N)
            answer += 1
    return answer

# 알고리즘 스터디 피드백
# O(N^2)의 시간복잡도라 통과 못할 줄 알았는데 통과했음 : section.pop(0)는 O(N), section.pop()은 O(1)
# 만약 section이 deque였다면 pop 연산이 O(1)로 가능했을텐데, 
# O(N)으로 해결하는 방법은 section 길이만큼 돌리고 만약 paint 구간에 해당하는 것 칠해주고 시작 paint 지점을 다시 갱신하는 방법이 있다.
# 진우나 유재의 코드를 보면 알수 있음
