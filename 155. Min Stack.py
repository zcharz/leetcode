# this could be more memory efficient
# using list of pairs or 2 lists
# for corresponding values and mins
# rather than linked list



class ListNode:
    def __init__(self, val=0, min=0, next=None):
        self.val = val
        self.min = min
        self.next = next


class MinStack:
    def __init__(self):
        self.min_ind = None
        self.head = None
        self.length = 0

    def push(self, val: int) -> None:
        if self.head != None:
            node = ListNode(val, min(val, self.head.min), self.head)
        else:
            node = ListNode(val, val, self.head)
        self.head = node
        self.length+=1

    def pop(self) -> None:
        self.length-=1
        self.head = self.head.next
        
    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min
        



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

stack = MinStack()

test = [1,2,3,4,5]
for i in test:
    stack.push(i)

for i in range(5):
    stack.push