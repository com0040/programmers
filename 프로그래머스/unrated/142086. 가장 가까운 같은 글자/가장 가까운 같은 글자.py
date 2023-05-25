def solution(s):
    answer,string = [-1 for i in s],['-1' for i in s]
    for idx1, j in enumerate(s):
        if j not in string:
            string[idx1] = j
        else:
            for idx2, k in enumerate(string):
                if k == j and idx1 != idx2:
                    answer[idx1] = idx1 - idx2
                    string[idx2] = '-1'
                    string[idx1] = j
    return answer