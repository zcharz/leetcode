from linkedlist import *

class Solution:
    def reorderList(self, head: ListNode) -> None:
        pass

sol = Solution()

head = toLinkedList([1,2,3,4])
sol.reorderList(head)
print(toList(head))

head = toLinkedList([1,2,3,4,5])
sol.reorderList(head)
print(toList(head))