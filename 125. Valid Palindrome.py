def isPalindrome(s: str) -> bool:
    start = 0
    end = len(s)-1

    s = s.lower()
    print(s)

    while start<=end:
        # print(s[start], s[end])

        if s[start] == s[end]:
            start+=1
            end-=1
            continue

        elif s[start] == ' ' or not s[start].isalnum():
            start+=1
            continue

        elif s[end] == ' ' or not s[end].isalnum():
            end-=1
            continue

        return False
    return True


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))


# neetcode solution
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l, r = 0, len(s) - 1
#         while l < r:
#             while l < r and not self.alphanum(s[l]):
#                 l += 1
#             while l < r and not self.alphanum(s[r]):
#                 r -= 1
#             if s[l].lower() != s[r].lower():
#                 return False
#             l += 1
#             r -= 1
#         return True

#     # Could write own alpha-numeric function
#     def alphanum(self, c):
#         return (
#             ord("A") <= ord(c) <= ord("Z")
#             or ord("a") <= ord(c) <= ord("z")
#             or ord("0") <= ord(c) <= ord("9")
#         )
