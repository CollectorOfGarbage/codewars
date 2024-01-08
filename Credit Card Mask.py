# return masked string
def maskify(cc):
    result = ""
    for i in range(len(cc)):
        if i < len(cc)-4:
            result = result + "#"
        else:
            result = result + cc[i]
    return result
            
print(maskify("4556364607935616"))