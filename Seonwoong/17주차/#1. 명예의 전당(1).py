
def solution(k, score):
    answer = []
    stack=[]
    day=len(score)

    for i in range(day):
        stack.append(score[i])
        stack.sort(reverse=True)

        if i<k:
            answer.append(stack[-1])
        else:
            answer.append(stack[k-1])

    return answer
