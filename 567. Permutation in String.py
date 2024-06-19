
# finding s1 in s2
def checkInclusion(s1: str, s2: str) -> bool:
    chars = {char: s1.count(char) for char in s1}
    l, r = 0, 0
    curr = {char: 0 for char in s1}    

    while r<len(s2):
        c = s2[r]
        # if diff character not in s1
        if c not in chars:
            r+=1
            l = r
            curr = {char: 0 for char in s1}
            continue

        # r character is in s1
        curr[c] +=1
        while curr[c] > chars[c]:
            curr[s2[l]]-=1
            l+=1

        # print(f'{l} {r}  {curr}')
        if r-l+1 == len(s1):
            return True
        r+=1

    return False


s1 = "ab"
s2 = "eidbaooo"

s1 = "adc"
s2 = "dcda"

s1 = "ky"
s2 = "ainwkckifykxlribaypk"

print(checkInclusion(s1,s2))