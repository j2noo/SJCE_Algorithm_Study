from collections import deque

def solution(s, skip, index):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    alphabet=deque(alphabet)
    answer = ''    
    for x in skip: alphabet.remove(x)

    for i in range(len(s)):
        answer+=alphabet[(alphabet.index(s[i])+index)%(len(alphabet))]

    return answer
