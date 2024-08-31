# lv2
# 시간 : 30분
def solution(s):
    isExist = [0] * 100_000
    answer = []
    li = s.split("},")
    num_li = []
    for st in li:
        st=st.replace('{','')
        st=st.replace('}','')
        num_li.append(list(map(int,st.split(','))))
                            
    sorted_li = sorted(num_li, key= lambda x : len(x))
    
    
    for li in sorted_li:
        for num in li:
            if isExist[num]==0:
                isExist[num]=1
                answer.append(num)
                break
    
    return answer

# 크기순 정렬
# idx마다, 새로 나오ㅡ는 원소를 튜플에 추가 -> O(N)
# 새로 나오는 원소인지 판별하는 법? -> O(N)
# -> O(N^2)