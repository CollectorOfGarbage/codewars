def filter_list(l):
    'return a new list with the strings filtered out'
    final_list = []
    for item in l:
        if type(item) == int:
            final_list.append(item)
    print(len(l))
    return final_list