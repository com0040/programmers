def solution(sizes):
    answer,jigap = 0,[[],[]]
    for i in sizes:
        i.sort()
        jigap[0].append(i[0])
        jigap[1].append(i[1])
    print(max(jigap[0])*max(jigap[1]))
    return max(jigap[0])*max(jigap[1])