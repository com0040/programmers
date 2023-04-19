def solution(n):
    answer = [int(i) for i in(str(n))]
    answer.sort(reverse=True)
    answer = [str(i) for i in answer]
    return int(''.join(answer))