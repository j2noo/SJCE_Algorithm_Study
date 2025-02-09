import math

s = input()
t = input()
ls = len(s)
lt = len(t)

lcm = math.lcm(ls, lt)

s = s * (lcm // ls)
t = t * (lcm // lt)

if s == t:
    print(1)
else:
    print(0)
