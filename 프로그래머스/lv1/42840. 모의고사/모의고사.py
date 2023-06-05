def solution(answers):
    # 각 수포자의 찍는 패턴을 정의합니다.
    pattern_1 = [1, 2, 3, 4, 5]
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 각 수포자의 정답 수를 저장할 변수를 초기화합니다.
    scores = [0, 0, 0]
    
    # 정답 배열을 순회하면서 각 수포자의 정답을 비교합니다.
    for i, answer in enumerate(answers):
        if answer == pattern_1[i % len(pattern_1)]:
            scores[0] += 1
        if answer == pattern_2[i % len(pattern_2)]:
            scores[1] += 1
        if answer == pattern_3[i % len(pattern_3)]:
            scores[2] += 1
    
    # 가장 많은 문제를 맞힌 점수를 계산합니다.
    max_score = max(scores)
    
    # 가장 많은 문제를 맞힌 사람들을 저장할 리스트를 초기화합니다.
    winners = []
    
    # 점수를 순회하면서 가장 많은 문제를 맞힌 사람들의 번호를 저장합니다.
    for i, score in enumerate(scores):
        if score == max_score:
            winners.append(i + 1)
    
    return winners
