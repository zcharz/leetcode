# from linkedlist import *
# from binarytree import *
import collections

test = [1,2,3,4,5,6]

for num in range(len(test)):

    if test[num] == 3:
        test.pop(num)

print(test)