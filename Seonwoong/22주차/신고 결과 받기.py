from collections import defaultdict

def solution(id_list, report,k):
    answer = []
    # 중복 신고 제거
    report = list(set(report))
    # user별 신고한 id 저장
    user = defaultdict(set)
    # user별 신고당한 횟수 저장
    cnt = defaultdict(int)
	
    for r in report:
        # report의 첫번째 값은 신고자id, 두번째 값은 신고당한 id
        a,b = r.split()
        # 신고자가 신고한 id 추가
        user[a].add(b)
        # 신고당한 id의 신고 횟수 추가
        cnt[b] += 1
    
    for i in id_list:
        result = 0
        # user가 신고한 id가 k번 이상 신고 당했으면, 받을 메일 추가
        for u in user[i]:
            if cnt[u]>=k:
                result +=1
        answer.append(result)
    return answer
