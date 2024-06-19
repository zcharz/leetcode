def partition(s: str) -> list[list[str]]:
    ret = []
    stack = []

    def backtrack(start, end):
        if end==len(s) and s[start:end]==s[start:end][::-1]:
            stack.append(s[start:end])
            ret.append(stack.copy())
            stack.pop()
            return
        
        elif end==len(s):
            return

        if s[start:end] == s[start:end][::-1]:
            stack.append(s[start:end])
            backtrack(end, end+1)
            stack.pop()
        backtrack(start, end+1)

    backtrack(0,1)
    return ret

test = 'aab'
print(partition(test))

