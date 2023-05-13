def solution(n, arr1, arr2):
    string, answer = '', []
    arr1 = [f'{i:0{n}b}' for i in arr1]
    arr2 = [f'{i:0{n}b}' for i in arr2]
    for a1,b1 in zip(arr1,arr2):
        for a2,b2 in zip(a1,b1):
            # print(a2,b2)
            if a2 == '0' and b2 == '0':
                string += ' '
            else:
                string += '#'
        # print(string)
        answer.append(string)
        string = ''
        
    return answer