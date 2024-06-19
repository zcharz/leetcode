def reverseBits(n: int) -> int:
    ret = 0
    c = 31

    # print(bin(n))

    while n!=0:
        ret += n%2*2**c
        c-=1
        n = n >> 1

    # for i in range(32)
    #     bit = (n >> i) & 1
    #     ret += (bit << (31 - i))

    # print(bin(ret))
    return ret


n = 43261596
print(reverseBits(n))