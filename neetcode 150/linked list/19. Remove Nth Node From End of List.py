from linkedlist import *

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        # O(n) solution
        # find the right node to remove by using 2 pointers
        # one shifted forwards to detect end 
        # other one back to be the nth last node
        dummy = ListNode(0, head)
        
        prev = dummy
        end = dummy.next
        for i in range(n):
            end = end.next

        while end != None:
            prev = prev.next
            end = end.next

        prev.next = prev.next.next
        return dummy.next


        # O(2n) solution
        # count the length, then find the right node to remove
        dummy = ListNode(0, head)

        count = 0
        curr = dummy
        while curr!=None:
            curr = curr.next
            count+=1
        
        find = count-n
        prev = dummy
        remove = dummy.next

        for i in range(find-1):
            prev = prev.next
            remove = remove.next

        prev.next = remove.next
        return dummy.next


sol = Solution()

head = toLinkedList([1,2,3,4,5])
n = 2
print(toList(sol.removeNthFromEnd(head, n)))

head = toLinkedList([1])
n = 1
print(toList(sol.removeNthFromEnd(head, n)))

head = toLinkedList([1,2])
n = 1
print(toList(sol.removeNthFromEnd(head, n)))