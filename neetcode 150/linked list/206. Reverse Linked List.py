from linkedlist import *


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        node = head
        curr = node.next
        node.next = None
        
        while node and curr:
            temp = curr.next

            curr.next = node
            node = curr
            curr = temp

        return node

    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        # TODO: recursive

        return node


sol = Solution()

head = toLinkedList([1,2,3,4,5])
print(toList(sol.reverseList(head)))