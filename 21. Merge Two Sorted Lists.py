from linkedlist import *

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:   
    head = ListNode()
    node = head

    while list1 and list2:
        #list1!=None and list2!=None
        if list1.val <= list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next
        node = node.next

    # if list -> true, not empty

    if list1:
        node.next = list1
    elif list2:
        node.next = list2
    
    return head.next
    

list1 = makeLL([1,2,4])
list2 = makeLL([1,3,4])


print(LL_to_list(mergeTwoLists(list1,list2)))





