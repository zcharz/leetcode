class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # O(n) memory
        mapping = dict()

        # O(n) time
        for s in strs:
            # O(m log m) time
            # O(m) memory per key
            # key = ''.join(sorted(s))

            # O(m) time
            # O(1) memory per key (always length 26)
            key = [0] * 26
            for c in s:
                key[ord(c)-ord('a')]+=1
            key = tuple(key)

            # group should point to the same list, if it exists
            # however if it doesn't assign it
            # no extra memory
            group = mapping.get(key, [])
            group.append(s)
            mapping[key] = group

            # could otherwise use defaultdict(list)
            # mapping[key].append(s)

        return list(mapping.values())


sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs))