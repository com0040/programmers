def solution(a, b, n):
    answer = 0
    while True:
        refill = (n // a) * b
        remain = n % a
        answer += refill 
        n = refill + remain
        if n // a <= 0:        
            print(refill, remain, n)
            return answer