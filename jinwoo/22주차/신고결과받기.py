
# 17qns
def solution(id_list, report, k):
    const = {}
    for idx, val in enumerate(id_list):
        const[val] = idx
    
    cnt = [[0] * 1000 for _ in range(1000)]
    for rep in report :
        user1,user2 = rep.split()
        cnt[const[user1]][const[user2]] = 1
    
    # j가 신고 당한 여부
    isBanned = [0] * 1000
    for j in range(len(id_list)):
        sum = 0
        for i in range(len(id_list)):
            sum+=cnt[i][j]
        if sum >= k:
            isBanned[j] = 1
            
    # 신고 알람 메일 카운트
    answer = []
    
    for id in id_list :
        sum=0
        idx = const[id]
        for j in range(len(id_list)):
            if cnt[idx][j] ==1 and isBanned[j]==1 :
                sum+=1
        answer.append(sum)
    return answer