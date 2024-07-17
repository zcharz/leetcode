from linkedlist import *


class Solution:
    # iterative solution
    def reverseList(self, head: ListNode) -> ListNode:        
        node = None
        curr = head
        
        while curr:
            temp = curr.next

            curr.next = node
            node = curr
            curr = temp

        return node

    # recursive solution
    def reverseList(self, head: ListNode) -> ListNode:
        def helper(node):
            if not node.next:
                return node, node
            head, tail = helper(node.next)
            tail.next = node
            tail = tail.next
            tail.next = None

            return head, tail

        return helper(head)[0] if head else None


sol = Solution()

head = toLinkedList([1,2,3,4,5])
print(toList(sol.reverseList(head)))