def solution(s):
    words = s.split(" ")
    answer = ""
    for i, word in enumerate(words):
        new_word = ""
        for j, c in enumerate(word):
            if j % 2 == 0:
                new_word += c.upper()
            else:
                new_word += c.lower()
        answer += new_word
        if i != len(words) - 1 and len(word) > 0 and word[-1] == "":
            answer += " "
        elif i != len(words) - 1:
            answer += " "
    return answer