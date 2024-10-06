def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def convert_to_base(n, k):
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(int(n % k))
        n //= k
    return ''.join(map(str, digits[::-1]))


def solution(n, k):
    # Step 1: 진법 변환
    base_k = convert_to_base(n, k)
    
    # Step 2: 0으로 나누기
    parts = base_k.split('0')
    
    print(parts)
    # Step 3: 소수 세기
    prime_count = 0
    
    # Check each part and its neighbors
    for i in range(len(parts)):
        if parts[i] == '':
            continue
            
        # Check if the current part is prime
        num = int(parts[i])
        if is_prime(num):
            prime_count += 1
        
    return prime_count
