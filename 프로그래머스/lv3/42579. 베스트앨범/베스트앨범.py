# v1
from collections import defaultdict

def solution(genres, plays):
    answer = []
    hash = defaultdict(list)
    for i, j in enumerate(zip(genres,plays)):
        if j[0] not in hash:
            hash[j[0]] = [[],[]]
        hash[j[0]][0].append(j[1])
        hash[j[0]][1].append(i)
        # print(hash)
    for key in hash:
        hash[key].append(sum(hash[key][0]))
    hash = dict(sorted(hash.items(), key=lambda x: x[1][-1], reverse=True))
    
    for key in hash:
        # hash[key][0] = sorted(hash[key][0],reverse = True)
        # hash[key][1] = sorted(hash[key][1],reverse = True)
        if len(hash[key][0]) > 1:
            print(hash[key][1][hash[key][0].index(max(hash[key][0]))],hash[key][0].index(max(hash[key][0])))
            answer.append(hash[key][1][hash[key][0].index(max(hash[key][0]))])
            hash[key][1].pop(hash[key][0].index(max(hash[key][0])))
            hash[key][0].pop(hash[key][0].index(max(hash[key][0])))
            answer.append(hash[key][1][hash[key][0].index(max(hash[key][0]))])
        else:
            answer.append(hash[key][1][hash[key][0].index(max(hash[key][0]))])
    # for key in hash:
    #     if len(hash[key][1][:2]) > 1:
    #         answer.append(hash[key][1][:2])
    #     else:
    #         answer.append(hash[key][1])
    # answer = sum(answer, [])
    print(hash)
    return answer