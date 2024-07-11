def solution(keymap, targets):
    # keymap에서의 알파벳과 해당 최소 인덱스를 각각 dic에 키, 값으로 넣어주기 
    dic={}
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            alphabet=keymap[i][j]
            if alphabet in dic.keys():
                dic[alphabet]=min(dic[alphabet], j+1)
            else:
                dic[alphabet]=j+1
         
    answer = []
    # targets에서 해당하는 점수 answer에 넣어주기
    for i in range(len(targets)):
        total=0
        for j in range(len(targets[i])):
            if targets[i][j] in dic.keys():
                total+=dic[targets[i][j]]
            else:
                total=-1
                break
        answer.append(total)
    
    return answer

# 소요시간 15분
# C언어 식으로 푼거같음, 시간복잡도 O(n^2) 나올듯
