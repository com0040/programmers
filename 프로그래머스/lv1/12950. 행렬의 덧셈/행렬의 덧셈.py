def solution(arr1, arr2):
    # answer = [x[i]+y[i] for x,y in zip(arr1,arr2) for i in range(len(x)) ]
    answer = []
    # print(len(answer))
    for index,(a,b) in enumerate(zip(arr1,arr2)):
        for i in range(len(a)):
            if i==0:
                answer.append([a[i]+b[i]])
            else:
                answer[index].append(a[i]+b[i])
    return answer