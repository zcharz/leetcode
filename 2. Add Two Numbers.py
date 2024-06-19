from linkedlist import *


# own solution
# messy code for edge cases
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    node1 = ListNode(0, l1)
    node2 = ListNode(0, l2)

    digit = ListNode(0)
    head = digit
    carry = False

    while node1.next and node2.next:
        # l1.next != None and l2.next != None

        node1 = node1.next
        node2 = node2.next

        val = node1.val+node2.val

        if carry:
            val+=1
        
        if val<10:
            carry = False
        else:
            val%=10
            carry = True  

        new = ListNode(val)

        digit.next = new
        digit = digit.next

    # now one of node1.next and node2.next is None
    def extend(digit, node, carry):
        digit.next = node.next
        digit = digit.next

        while carry and digit.next:
            digit.val+=1

            if digit.val<10:
                carry = False
            else:
                digit.val%=10
                digit = digit.next
        
        # possible last element
        if carry:
            digit.val+=1

            if digit.val>=10:
                digit.val%=10
                digit.next = ListNode(1)


    if node1.next:
        extend(digit, node1, carry)
    elif node2.next:
        extend(digit, node2, carry)
    elif carry:
        digit.next = ListNode(1)


    return head.next


# l1 = makeLL([2,4,3])
# l2 = makeLL([5,6,4])

# l1 = makeLL([9,9,9,9,9,9,9])
# l2 = makeLL([9,9,9,9])

l1 = makeLL([5])
l2 = makeLL([5])


print(LL_to_list(addTwoNumbers(l1,l2)))




# neetcode solution
# WAY more concise
# 

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    cur = dummy

    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        # new digit
        val = v1 + v2 + carry
        carry = val // 10
        val = val % 10
        cur.next = ListNode(val)

        # update ptrs
        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next