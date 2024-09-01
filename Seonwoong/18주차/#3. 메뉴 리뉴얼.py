from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course:
        comb_list = list()

        for order in orders:
            comb_list += combinations(sorted(order), c)

        count = Counter(comb_list).most_common()        
        # print(count)
        answer += [l[0] for l in count if (l[1] == count[0][1] and l[1] > 1)]

    #print(answer)
    answer = [''.join(a) for a in sorted(answer)]

    return answer

# 이걸 어케 이렇게 풀지..? 파이써닉 코드는 이렇게 짜는 것인가..
# 출처: https://sumim.tistory.com/entry/프로그래머스-메뉴-리뉴얼-2021-Kakao-Blind-Recruitment [지식창고:티스토리]
