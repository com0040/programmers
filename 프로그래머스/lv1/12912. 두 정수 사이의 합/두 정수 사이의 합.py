def solution(a, b):
    answer = [a,b]
    answer.sort()
    return sum([i for i in range(answer[0],answer[1]+1)])