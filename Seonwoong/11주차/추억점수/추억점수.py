def solution(name, yearning, photo):
    dic = {name[i]: yearning[i] for i in range(len(name))}
    answer = []
    for case in photo:
        score = 0
        for person in case:
            if person in dic:
                score += dic[person]
        answer.append(score)
    return answer
