def solution(s):
    s=s[1:-1]
    s=s.replace('{', '[')
    s=s.replace('}', ']')

    x,arr,tmp=[],[],''
    flag=0
    for i in range(len(s)):
        if s[i]=='[':
            flag=1
            continue
        elif s[i]==']':
            flag=0
            arr.append(int(tmp))
            x.append(arr)
            arr,tmp=[],''
        else:
            if s[i] !=',': tmp+=s[i]
            else: 
                if flag==1: arr.append(int(tmp))
                tmp=''

    x=sorted(x,key=lambda s:len(s))    
    answer=x[0]

    for i in range(1,len(x)):
        complement=list(set(x[i])-set(x[i-1]))
        answer.append(complement[0])

    return answer
