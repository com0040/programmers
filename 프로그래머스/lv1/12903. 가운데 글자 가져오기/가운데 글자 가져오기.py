def solution(s):
    if len(s) == 1 or len(s) == 2:
        return s
    for i in range(len(s)):
        s = s[1:-1]
        if len(s) == 1 or len(s) == 2:
            return s