from linkedlist import *
import heapq


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        key = 0
        dummy = ListNode()
        heap = []
        curr = dummy

        for node in lists:
            if not node: continue
            heapq.heappush(heap, (node.val, key, node))
            key+=1

        while heap:
            node = heapq.heappop(heap)[2]
            curr.next = node
            curr = curr.next
            
            if not node.next: continue
            heapq.heappush(heap, (node.next.val, key, node.next))
            key+=1

        return dummy.next


sol = Solution()

lists = [toLinkedList([1,4,5]),toLinkedList([1,3,4]),toLinkedList([2,6])]
print(toList(sol.mergeKLists(lists)))

lists = [toLinkedList([])]
print(toList(sol.mergeKLists(lists)))

lists = []
print(toList(sol.mergeKLists(lists)))