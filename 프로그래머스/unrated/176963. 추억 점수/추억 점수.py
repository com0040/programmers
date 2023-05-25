def solution(name, yearning, photo):
    answer, chu = [0 for i in range(len(photo))], {}
    for person, score in zip(name,yearning):
        chu[person] = score
    for idx, pic in enumerate(photo):
        for ture in pic:
            if ture in chu:
                answer[idx] += chu.get(ture)
    return answer