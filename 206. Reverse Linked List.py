# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:

    if head == None:
        return
    
    def recur(node: ListNode):
        if node.next==None:
            # this is the new head
            return node
        else:
            head = recur(node.next)

            #find last node
            n = head
            while n.next != None:
                n = n.next
            n.next = node

            node.next = None

            return head
            
    return recur(head)



#debug 

node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

def printLL(node):
    if node==None:
        return []
    
    l = [node.val]
    l.extend(printLL(node.next))
    return l

print(printLL(node1))

print( printLL(reverseList(node1)))