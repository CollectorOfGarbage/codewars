def snail(snail_map):
    result = []
    while len(snail_map) > 0:
        result += snail_map[0]
        del snail_map[0]
        if len(snail_map) > 0:
            for i in snail_map:
                result.append(i[-1])
                del i[-1]
            if snail_map[-1]:
                result += snail_map[-1][::-1]
                del snail_map[-1]
            for i in reversed(snail_map):
                result.append(i[0])
                del i[0]
    return result


import pytest

snail([[1,2,3],[4,5,6],[7,8,9]])

