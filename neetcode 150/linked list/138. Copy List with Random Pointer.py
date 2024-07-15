class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        # intitializing edge case
        # rather than using dict.get(key, None)
        # runs faster here
        new = { None: None }
        node = head
        while node:
            new[node] = Node(node.val)
            node = node.next

        node = head
        # for node in new:
        while node:
            # new[node].next = new.get(node.next, None)
            # new[node].random = new.get(node.random, None)
            new[node].next = new[node.next]
            new[node].random = new[node.random]
            node = node.next
        # return new.get(head, None)
        return new[head]
