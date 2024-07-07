from linkedlist import *

class Solution:
    def reorderList(self, head: ListNode) -> None:

        
        curr = head

        while curr and curr.next and curr.next.next:
            seclast = curr
            while seclast.next.next:
                seclast = seclast.next
            
            temp = curr.next
            curr.next = seclast.next
            seclast.next = None
            curr.next.next = temp
            curr = curr.next.next

        return head

sol = Solution()

head = toLinkedList([1,2,3,4])
sol.reorderList(head)
print(toList(head))

head = toLinkedList([1,2,3,4,5])
sol.reorderList(head)
print(toList(head))