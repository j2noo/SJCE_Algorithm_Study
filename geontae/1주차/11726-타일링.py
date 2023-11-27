n = int(input())
dp = [-1]*1010


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        if (dp[n] != -1):
            return dp[n]
        else:
            dp[n] = fibo(n-2) + fibo(n-1)
            dp[n] %= 10007
            return dp[n]


result = fibo(n)
print(result)
