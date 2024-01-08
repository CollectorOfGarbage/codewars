def solution(s):
    solution = []
    for i in range(len(s)):
        if i%2 != 0: 
            solution.append(s[i-1:i])
    if len(s)%2 != 0: solution.append(s[-1] + '_')
    return solution
    
        


solution('abc')
solution('abcdef')
solution('abcdefg')
solution('abcdefgh')
solution('abcdefghi')
solution("x")
solution("")