def solution(n):
    answer = n **(1/2)
    if answer == int(answer):
        return (answer+1)**2
    else:
        return -1
