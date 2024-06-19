def isAnagram(s: str, t: str) -> bool:
        
    from collections import defaultdict

    if len(s) != len(t):
        return False
    
    count_s, count_t = defaultdict(int), defaultdict(int)
    for i in s:
        count_s[i]+=1
    for i in t:
        count_t[i]+=1

    for i in s:
        if count_s[i] != count_t[i]:
            return False
    
    return True

    # countS, countT = {}, {}

    # for i in range(len(s)):
    #     countS[s[i]] = 1 + countS.get(s[i], 0)
    #     countT[t[i]] = 1 + countT.get(t[i], 0)
    # return countS == countT