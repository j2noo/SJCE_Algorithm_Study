def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers)):
        x=numbers[i]
        while stack and numbers[stack[-1]] < x:
            answer[stack[-1]] = x
            stack.pop()
        stack.append(i)
        
    return answer
