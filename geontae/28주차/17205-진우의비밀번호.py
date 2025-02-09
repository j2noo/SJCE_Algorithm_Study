n = int(input())
pw = input()

# n자리일때 첫번째 자리를 a->b 바꾸는데 드는 시간
# n == 1 : 1 + 1 (a, b)
# n == 2 : 1 + 26 + 1 (a, a.., b)
# n == 3 : 1 + 26 * 27 + 1 (a, aa, aaa.., b)
# n == 4 : 1 + 26 * 27 + 1 (a, aa, aaa, aaaa... ,