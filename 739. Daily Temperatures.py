# brute force O(n^2) solution
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    ret = []

    for i in range(len(temperatures)):
        c = 0
        for j in range(i+1, len(temperatures)):
            if temperatures[i]<temperatures[j]:
                c = j-i
                break
        ret.append(c)
        
    return ret

# O(2n) worst case
# n for iteration
# up to n pops (only occurs once)
# stack is monotonic decreasing order (only decreases)
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    ret = [0 for i in range(len(temperatures))]
    stack = []

    for i, temp in enumerate(temperatures):
        while stack and temp>stack[-1][0]:
            prevtemp, prevind = stack.pop()
            ret[prevind] = i-prevind
        stack.append( (temp, i) )

    return ret


temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))
