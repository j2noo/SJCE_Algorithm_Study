# 9분
# lv2
def solution(book_time):
    cnt_li = [0] * 1500
    for s,e in book_time:
        hour, minute = map(int,s.split(":"))
        s = hour*60 + minute
        
        hour, minute = map(int,e.split(":"))
        e = hour*60 + minute+10
        
        print(s,e)
        for i in range(s,e):
            cnt_li[i]+=1
        
    return max(cnt_li)
    
# 실제 종료시간 + 10분
# 특정 시점에 겹치는 횟수?!
# 시간복잡도 1000^2