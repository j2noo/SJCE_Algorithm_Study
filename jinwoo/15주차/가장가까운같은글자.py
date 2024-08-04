# 7분
# lv1
def solution(s):
    # dic에 최근 나온 인덱스를 저장
    dic = {}
    ans = []
    for ch in range(ord('a'),ord('z')+1):
        dic[chr(ch)] = -1
    
    for idx,ch in enumerate(s):
        if dic[ch]==-1 :
            ans.append(dic[ch])
        else :
            ans.append(idx - dic[ch])
        dic[ch] = idx
        
    return ans

# 26개짜리 딕셔너리