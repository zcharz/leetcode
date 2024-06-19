def isValid(s: str) -> bool:
    while True:
        prev = len(s)
        print(s)
        s = s.replace('()', '')
        s = s.replace('[]', '')
        s = s.replace('{}', '')
        if len(s) == prev:
            return False
        if s == '':
            return True

    return s==''

    # neetcode solution
    # Map = {")": "(", "]": "[", "}": "{"}
    #     stack = []

    #     for c in s:
    #         if c not in Map:
    #             stack.append(c)
    #             continue
    #         if not stack or stack[-1] != Map[c]:
    #             return False
    #         stack.pop()

    #     return not stack


if __name__ == '__main__':
    #x = '()'
    #x = '(([]){})'
    x = '[({(())}[()])]'
    print(isValid(x))