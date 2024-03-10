s = input()
ret = ""

idx = 0
while idx < len(s):
    if s[idx] == 'X':
        if s[idx: idx + 4] == "XXXX":
            ret += "AAAA"
            idx += 4
        elif s[idx: idx + 2] == "XX":
            ret += "BB"
            idx += 2
        else:
            ret = "-1"
            break
    else:
        ret += "."
        idx += 1

print(ret)