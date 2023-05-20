def solution(array, commands):
    answer, cnt= [],[]
    for cuts in commands:    
        print(cuts)
        answer.append(sorted(array[cuts[0]-1:cuts[1]])[cuts[2]-1])
        print(sorted(array[cuts[0]-1:cuts[1]])[0])
    return answer