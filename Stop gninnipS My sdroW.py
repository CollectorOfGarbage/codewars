def spin_words(sentence):
    sentence = sentence.split(" ")
    final = ""
    for i, word in enumerate(sentence):
        if len(word) >= 5:
            final += word[::-1]
        else:
            final += word
        if i == len(sentence) - 1:
            break
        else:
            final += " "
    return final