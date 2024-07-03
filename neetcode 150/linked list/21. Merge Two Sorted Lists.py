from linkedlist import *

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = ListNode()
        curr = head

        while list1 and list2:
            if list1.val <list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2
        return head.next


sol = Solution()
    
list1 = toLinkedList([1,2,4])
list2 = toLinkedList([1,3,4])

print(toList(sol.mergeTwoLists(list1,list2)))





