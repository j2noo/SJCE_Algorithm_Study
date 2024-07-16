dp=[0]*5000001
def solution(e, starts):
    
    #약수의 개수 만큼 채우기 -> 계속 90점 떠서 검색함 : https://inspirer9.tistory.com/436
    for i in range(2,e+1):
        for j in range(1,min(e//i+1,i)):
            dp[i*j]+=2
    for i in range(1,int(e**0.5)+1):
        dp[i*i]+=1
        
    answer = []
    #숫자와 약수 개수를 리스트로 채우기
    arr=[(i,dp[i]) for i in range(min(starts),e+1)]
    
    #약수 개수 많은 순서로 정렬하기
    arr.sort(key=lambda x:(-x[1]))
    
    #start의 시작값부터 arr리스트의 첫 값(약수가 최대인 개수의 해당하는 수)랑 비교하여 최대 개수 찾기
    for i in starts:
        for y in arr:
            if i<=y[0]:
                answer.append(y[0])
                break
    
    return answer

# 이 코드가 90점 코드였는데 다시 제출하니까 아슬하게 마지막 테케 통과함.. 이건 100점 코드는 아닌듯
