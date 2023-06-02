def solution(k, score):
    answer,legend = [],[]
    for day in score:
        if len(legend) < k:
            legend.append(day)
            legend = sorted(legend)
        else:
            if day >= min(legend):
                legend = sorted(legend)
                legend.pop(0)
                legend.append(day)
                legend = sorted(legend)
        answer.append(min(legend))
    return answer