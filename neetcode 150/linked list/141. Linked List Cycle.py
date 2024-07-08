from linkedlist import *

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False


# sol = Solution()

# head = toLinkedList([3,2,0,-4])
# print(sol.hasCycle(head))