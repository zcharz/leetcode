def letterCombinations(digits: str) -> list[str]:
    if not len(digits):
        return []

    letters = {2: {'a', 'b', 'c'}, 3: {'d', 'e', 'f'}, 4: {'g', 'h','i'}, 5: {'l', 'j', 'k'}, 6: {'o', 'm', 'n'}, 7: {'r', 'q', 'p', 's'}, 8: {'t', 'u', 'v'}, 9: {'w', 'x', 'y', 'z'}}
    print(letters)

    ret = []
    stack = []
    c = 0

    def dfs(c):
        if c==len(digits):
            ret.append(''.join(stack))
            return

        for char in letters[int(digits[c])]:
            stack.append(char)
            dfs(c+1)
            stack.pop()

    dfs(c)
    return ret


print(letterCombinations('23'))