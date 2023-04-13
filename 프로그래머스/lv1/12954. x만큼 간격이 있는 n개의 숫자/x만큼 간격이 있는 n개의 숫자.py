def solution(x, n):
    if x == 0:
        return [0 for i in range(n)]
    if x > 0:
        answer = [i for i in range(x,x*n+1,x)]
    elif x < 0:
        answer = [i for i in range(x,x*n-1,x)]
    return answer