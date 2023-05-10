def solution(s, n):
    answer = ''
    large = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small = 'abcdefghijklmnopqrstuvwxyz'
    for i in s:
        if i in large:
            if (large.find(i)+n) >= len(large):
                answer += large[(large.find(i)+n-26)]
            else:
                answer += large[large.find(i)+n]
        elif i in small:
            if (small.find(i)+n) >= len(small):
                answer += small[(small.find(i)+n-26)]
            else:
                answer += small[small.find(i)+n]
        else:
            answer += ' '
    return answer