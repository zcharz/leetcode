# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# each function needs to be O(1) time

class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        if len(self.stack):
            # self.stack.append((val, min(self.stack[-1][1], val)))
            self.stack.append(val)
            self.mins.append(min(self.mins[-1], val))
        else:
            # self.stack.append((val, val))
            self.stack.append(val)
            self.mins.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        # return self.stack[-1][0]
        return self.stack[-1]

    def getMin(self) -> int:
        # return self.stack[-1][1]
        return self.mins[-1]

stack = MinStack()
# stack.push(6)
# for i in range(5):
#     stack.push(i)
# stack.push(-1)
# stack.push(4)

stack.push(0)
stack.push(1)
stack.push(0)
print(stack.stack)