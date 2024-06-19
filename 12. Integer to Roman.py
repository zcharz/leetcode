def intToRoman(num: int) -> str:
    val = dict([(1, 'I'), (5, 'V'), (10, 'X'), (50, 'L'), (100, 'C'), (500, 'D'), (1000, 'M')])
    ret = ''
    #1 <= num <= 3999

    while num > 0:
        n = num
        c = 0
        while n >= 10:
            c+=1
            n = n // 10
        # n = first digit
        # 10^cth place ie c = 2 -> n is at the 100s place
        add = ''

        # greatest key for main values
        ckey = 1
        for key in val:
            if key >= ckey and key <= num:
                ckey = key

        # previous key (lesser key) for increments
        pkey = 1
        for key in val:
            if key < ckey:
                pkey = key

        # next key (greater key) for increments
        nkey = 1
        for key in val:
            if key > ckey:
                nkey = key
                break

        if n == 4:
            add = val[ckey]+val[nkey]
        elif n == 9:
            add = val[pkey]+val[nkey]
        else:
            temp = n*(10**c)
            add = add + (temp//ckey)*val[ckey]
            temp = temp - (temp//ckey)*ckey
            add = add + (temp//pkey)*val[pkey]
        
        ret = ret + add
        num = num - n*(10**c)

    return ret

if __name__ == '__main__':
    x = 1994
    print(str(x) + ' = ' + intToRoman(x))