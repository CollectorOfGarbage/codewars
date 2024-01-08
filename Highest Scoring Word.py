def letter_score(letter):
    return ord(letter) - ord('a') + 1


def high(x):
    words = x.split(" ")
    scores = []
    for i, word in enumerate(words):
        score = 0
        for letter in word:
            score += letter_score(letter)
        scores.append(score)
    return words[scores.index(max(scores))]
        

print(high('man i need a taxi up to ubud'))