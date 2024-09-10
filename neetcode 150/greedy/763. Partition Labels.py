class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        ret = []
        last_appear = {c:i for i, c in enumerate(s)}

        start, end = -1, 0
        for i in range(len(s)):
            end = max(end, last_appear[s[i]]) 
            if i == end:
                ret.append(i-start)
                start = end

        return ret



sol = Solution()

s = "ababcbacadefegdehijhklij"
print(sol.partitionLabels(s))

s = "eccbbbbdec"
print(sol.partitionLabels(s))