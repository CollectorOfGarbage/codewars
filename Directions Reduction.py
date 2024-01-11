def dir_reduc(arr):
    opposites = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    new_arr = []
    for i in arr:
        if new_arr and new_arr[-1] == opposites[i]:
            new_arr.pop()
        else:
            new_arr.append(i)
    return new_arr
    
    
    
print(dir_reduc(["NORTH", "WEST", "NORTH", "SOUTH", "EAST"]))