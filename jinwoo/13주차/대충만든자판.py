def solution(keymap, targets):
    answer = []

    dic = {}
    for i in range(26):
        ch = chr(ord('A')+i)
        dic[ch]=999
    
    for key in keymap :
        for i in range(len(key)):
            dic[key[i]] = min(dic[key[i]], i+1)
    
    for target in targets:
        sum = 0
        for i in range(len(target)):
            sum += dic[target[i]]
        if sum>900:
            sum=-1
        answer.append(sum)
    print(dic)
    return answer

# {'A' : cnt} -> 26개, min값으로