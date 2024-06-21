from linkedlist import *


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:

    count = 0
    node = head
    while node!= None:
        node = node.next
        count+=1
    
    n = count-n

    node = head
    c = 0

    while c<n:
        node = node.next
        c+=1
    # node is the one to be removed

    prev = head
    m = 0
    while m<n-1:
        prev = prev.next
        m+=1

    if prev == node:
    # node to remove is the first one
        return head.next

    prev.next = node.next

    return head


test = [1,2,3,4,5]

head = makeLL(test)

print(LL_to_list(removeNthFromEnd(head, 2)))




# neetcode solution
# 2 pointer, end pointer to see when to end iteration
# use dummy node and n+1 to displace front node
# so that iteration stops at node before target of deletion

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    # delete
    left.next = left.next.next
    return dummy.next


