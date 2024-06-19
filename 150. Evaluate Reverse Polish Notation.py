import collections


# attempt at backwards iteration for stack
# result isnt correct due to nested operations
def evalRPN(tokens: list[str]) -> int:
    stack = collections.deque()
    c = len(tokens)-1

    # while tokens is not empty
    while len(tokens)>1:
        if c>=len(tokens):
            c-=1
            continue

        # if the character is a sign (operation)
        # and the previous one is a number
        # match them and push to stack
        if not tokens[c].isalnum() and tokens[c-1].isalnum():
            stack.append((tokens[c], tokens[c-1]))
            tokens.pop(c-1)
            tokens.pop(c-1)
        # nested part
        else:
            # count for ??????
            c-=1
    
    ret = tokens[0]

    print(stack)
    print(tokens)

    while stack:
        curr =  stack.pop()
        op = curr[0]
        num = curr[1]
        ret = eval(f'{ret} {op} {num}')
    return ret



# forward iteration solution
def evalRPN(tokens: list[str]) -> int:
    stack = collections.deque()
    stack.append(tokens[0])

    c = 1
    while c<len(tokens):
        # print(stack)
        
        # if the new token is an operation, do it on the first 2 unimbers and add back that number
        if not tokens[c].isalnum() and len(tokens[c])==1:
            a = stack.pop()
            b = stack.pop()
            element = int(eval(f'{b} {tokens[c]} {a}'))

            # stack.append(eval(f'{stack.pop()} {tokens[c]} {stack.pop()}'))
            stack.append(element)
            
        # add numbers to stack to do operations later
        else:
            stack.append(tokens[c])
            
        c+=1
    
    return int(stack[0])



tokens =  ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))