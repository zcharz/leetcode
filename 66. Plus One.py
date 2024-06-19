def plusOne(digits: list[int]) -> list[int]:

    # if list is empty:
    if not digits:
        return []
    
    digits[len(digits)-1]+=1

    c = len(digits)-1
    digits[c]


    while c>0:
        if digits[c] == 10:
            digits[c] = 0
            digits[c-1]+=1
            c-=1
        else:
            break

    if digits[0] == 10:
        digits[0] = 0
        digits = [1] + digits

    return digits

