# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def toList(node):
    ret = []
    while node:
        ret.append(node.val)
        node = node.next
    return ret


def toLinkedList(l: list) -> ListNode:
    head = ListNode()
    node = head
    for e in l:
        new_node = ListNode(e)
        node.next = new_node
        node = node.next
    return head.next
