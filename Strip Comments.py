def strip_comments(strng, markers):
    strng = strng.split('\n')
    for i in range(len(strng)):
        for j in range(len(strng[i])):
            if strng[i][j] in markers:
                strng[i] = strng[i][:j].rstrip()
                break
    return '\n'.join(strng)

#print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))
print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !#apples",['#', '!']))
#strip_comments('a #b\nc\nd $e f g', ['#', '$'])
#strip_comments(' a #b\nc\nd $e f g', ['#', '$'])