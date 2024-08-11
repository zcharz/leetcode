from linkedlist import *

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        curr = dummy

        def reverseK(start, end):
            curr = start
            prev = end

            while curr != end:
                temp = curr.next

                curr.next = prev
                prev = curr
                curr = temp

            return start, prev

        while True:
            last = curr
            for i in range(k):
                if last.next:
                    last = last.next
                else:
                    return dummy.next
            
            nextk, flippedhead = reverseK(curr.next, last.next)
            curr.next = flippedhead
            curr = nextk


sol = Solution()

# head = toLinkedList([1,2,3,4,5])
# k = 2
# print(toList(sol.reverseKGroup(head, k)))


# head = toLinkedList([1,2,3,4,5])
# k = 3
# print(toList(sol.reverseKGroup(head, k)))


head = toLinkedList([1,2])
k = 2
print(toList(sol.reverseKGroup(head, k)))