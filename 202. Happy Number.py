def isHappy(n: int) -> bool:
    seen = set()

    curr = n
    
    while curr != 1:
        seen.add(curr)
        sum = 0

        # sum of squares loop
        temp = curr
        while temp>0:
            digit = temp%10
            sum+=digit*digit

            if temp<10:
                break

            temp=temp//10
            # int div
        
        if sum in seen:
            return False

        curr = sum  
    
    return True

    



sum = 0
temp = 13
while temp>0:
    digit = temp%10
    sum+=digit*digit

    if temp<10:
        break

    temp=temp//10

print(sum)