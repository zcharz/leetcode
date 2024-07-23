from linkedlist import *


class Solution:
    def reorderList(self, head: ListNode) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None
        prev = None
        while head2: 
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp
        head2 = prev
            
        dummy = ListNode()
        node = dummy
        while head or head2: 
            if head: 
                node.next = head
                head = head.next
                node = node.next
            if head2:
                node.next = head2
                head2 = head2.next
                node = node.next
        return dummy.next
    
sol = Solution()

head = toLinkedList([1,2,3,4])
print(toList(sol.reorderList(head)))

head = toLinkedList([1,2,3,4,5])
print(toList(sol.reorderList(head)))