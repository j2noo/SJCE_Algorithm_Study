# 풀이에 걸린 시간: 7분 10초
# 풀이에 사용한 접근: 색을 칠해야하는 부분부터 시작하여 페인트 칠하는게 가장 이득이다 (그리디).

def solution(n, m, section):
    answer = 1

    start = section[0]
    for i in range(1, len(section)):
        paintNumber = section[i]

        if paintNumber - start + 1 > m:
            answer += 1
            start = paintNumber

    return answer