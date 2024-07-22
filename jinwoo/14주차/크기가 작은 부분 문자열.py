# 4분 30초
# lv1
def solution(t, p):
    answer = 0

    l = len(p)
    for i in range(len(t)-l+1):
        parse = t[i:i+l]
        if int(parse) <= int(p):
            answer+=1
    return answer

# ez