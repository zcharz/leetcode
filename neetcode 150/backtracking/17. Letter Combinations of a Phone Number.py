class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits: return []
        ret, stack = [], []
        charmap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['q', 'p', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        def dfs(i):
            if i==len(digits):
                ret.append(''.join(stack))
                return
            
            for c in charmap[digits[i]]:
                stack.append(c)
                dfs(i+1)
                stack.pop()

        dfs(0)
        return ret


sol = Solution()

digits = '23'
print(sol.letterCombinations(digits))

digits = '2'
print(sol.letterCombinations(digits))