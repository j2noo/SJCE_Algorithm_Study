# 9분
# lv1
def solution(s, skip, index):
    answer = ''
    
    for word in s:
        for i in range(index):
            while(True):
                word = ord(word)+1
                if word > ord('z'):
                    word = ord('a')
                word = chr(word)
                if not word in list(skip):
                    break
        answer+=word
            
    return answer
# 구현..