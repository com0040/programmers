def solution(t, p):
    answer,string = 0, ''
    for i in t:
        string += i
        if len(string) == len(p):
            if int(p) >= int(string):
                answer += 1
        if len(string) >= len(p):
            string = string[1:]
    return answer