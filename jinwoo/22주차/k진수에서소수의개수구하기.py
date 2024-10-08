# 15분
def isPrime(num):
    # 111111111111 이런수는 소수인지 어케알아
    # 100만이 2진수로 나타내면 20자리임
    # 3진수는 17자리, 루트씌우면  9자리/
    if num == 1:
        return 0
    for div in range(2,int(num**0.5)+1):
        if num % div ==0 :
            return 0
    return 1

def solution(n, k):
    answer =0
    trans = ""
    while(n>0):
        trans =  str(n%k) + trans 
        n = n // k
    print(trans)
    num_li = trans.split("0")
    for num in num_li :
        if num!='':
            answer += isPrime(int(num))
    return answer

# k진법 번환후0으로 split
# 문자열뒤집기>