# from linkedlist import *
# from binarytree import *
import collections


test = [1,2,3,4,5,6,7,8]

for i in range(len(test)):
    test.pop()
    print(i)


n1, n2 = 1, 2
n1, n2 = n2, n1+n2
print(n1, n2)

print(ord('a'))


x = [0,0,0,0,0,0]
y = [0 for i in range(6)]
print(x==y)

x= [0]*26
x[0] +=1
y = x
print(x)
print(y)

s = '1234'
print(s[0:1])