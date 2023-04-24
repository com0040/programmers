def solution(arr, divisor):
    answer = [a for a in arr if a % divisor == 0]
    answer.sort()
    print(answer)
    if all(elem == -1 for elem in answer):
        return [-1]
    return answer