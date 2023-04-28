def solution(numbers):
    answer = [0,1,2,3,4,5,6,7,8,9]
    for i in numbers:
        if i in answer:
            print(answer.pop(answer.index(i)))
    return sum(answer)