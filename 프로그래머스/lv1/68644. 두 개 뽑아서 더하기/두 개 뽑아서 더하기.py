def solution(numbers):
    answer = []
    new = numbers
    while new:
        a = new.pop(0)
        for i in new:
            answer.append(a+i)
        print(numbers)
    answer = sorted(list(set(answer)))
    return answer