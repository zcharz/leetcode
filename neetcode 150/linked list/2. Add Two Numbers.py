from linkedlist import *

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1+v2+carry
            carry = val//10 # 1 if val>=10
            val%=10

            curr.next = ListNode(val)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


sol = Solution()


l1 = toLinkedList([2,4,3])
l2 = toLinkedList([5,6,4])

print(toList(sol.addTwoNumbers(l1, l2)))