def groupAnagrams(strs: list[str]) -> list[list[str]]:
    keylist = set([''.join(sorted(s)) for s in strs])
    # O(m*nlogn)
    # m = length of strs
    # n = average length of string

    anagram = {key: list() for key in keylist}

    for s in strs:
        for key in anagram:
            if ''.join(sorted(s)) == key:
                anagram[key].append(s)

    ret = [val for val in anagram.values()]
    return ret

    # O(m*n) solution:
    # for each string create a list that counts how many of each letter
    # use each different count list as a key for a dict
    # each string with same count list gets put into the same list in the dict
    # return all values in dict (all groups of strings)

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
