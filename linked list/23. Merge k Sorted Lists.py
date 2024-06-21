from linkedlist import *


# time complexity O(kN)
# k different lists each time
# total N values

def mergeKLists(lists: list[ListNode]) -> ListNode:
    head = ListNode()
    curr = head

    # remove empty lists before iteration
    remove_c = 0
    while remove_c < len(lists):
        if lists[remove_c] == None:
            lists.pop(remove_c)
            continue
        remove_c+=1


    # while lists isn't empty
    while lists: 
        min_ind = 0
        min_node = lists[0]

        for i, node in enumerate(lists):
            if node.val<min_node.val:
                min_node = node
                min_ind = i

        curr.next = min_node
        curr = curr.next

        lists[min_ind] = lists[min_ind].next
        curr.next = None

        remove_c = 0
        while remove_c < len(lists):
            if lists[remove_c] == None:
                lists.pop(remove_c)
                continue
            remove_c+=1
    
    return head.next
            


test = [[1,4,5],[1,3,4],[2,6]]

for i in range(len(test)):
    test[i] = makeLL(test[i])

print(LL_to_list(mergeKLists(test)))



# neetcode solution
# O(logk N)
# merging 2 sorted lists at a time, reduce iteration over k (k comparisons) to log k

def mergeKLists(lists: list[ListNode]) -> ListNode:
    if not lists or len(lists) == 0:
        return None

    while len(lists) > 1:
        mergedLists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            mergedLists.append(mergeList(l1, l2))
        lists = mergedLists
    return lists[0]

def mergeList(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    return dummy.next