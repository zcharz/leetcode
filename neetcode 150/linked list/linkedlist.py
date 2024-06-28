# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def LL_to_list(node):
    if node==None:
        return []
    
    l = [node.val]
    l.extend(LL_to_list(node.next))
    return l


def makeLL(l: list) -> ListNode:
    head = ListNode()
    node = head
    for e in l:
        new_node = ListNode(e)
        node.next = new_node
        node = node.next
    return head.next
