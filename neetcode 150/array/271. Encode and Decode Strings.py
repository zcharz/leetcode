class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        ret = ''
        for s in strs:
            ret+=(str(len(s))+';'+s)
        return ret
        

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        ret = []
        i = 0
        
        # neetcode nested while loops
        while i < len(str):
            j = i
            while str[j] != '#':
                j += 1
            length = int(str[i:j])
            i = j + 1
            j = i + length
            ret.append(str[i:j])
            i = j


        # my messy ahh code
        # while str:
        #     for i, c in enumerate(str):
        #         if c != ';':
        #             continue
        #         length = int(str[:i])
        #         s = str[i+1:i+1+length]
        #         ret.append(s)
        #         str = str[i+1+length:]
        #         break

        return ret



sol = Solution()


strs = ["we", "say", ":", "yes"]
encoded = sol.encode(strs)
print(sol.decode(encoded))