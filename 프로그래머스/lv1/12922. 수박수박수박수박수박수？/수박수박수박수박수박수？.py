def solution(n):
    answer = '수박'*(n//2) if n % 2 == 0 else ('수박'*(n//2+1))[:-1]
    return answer