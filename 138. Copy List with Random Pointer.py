class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# 4 passes
# 1: assign each node to an index
# 2: assign each node the random index
# 3: make each new node based on iteration
# 4: link everything together using nodes from new, info from 1 and 2

def copyRandomList(self, head: Node) -> Node:
    adj = dict()
    c = 0
    curr = head
    while curr:
        adj[curr] = c
        c+=1
        curr = curr.next

    # matches the nth element with the random's index
    random = dict()
    c = 0
    curr = head
    while curr:
        if curr.random:
            random[c] = adj[curr.random]
        c+=1
        curr = curr.next

    newnodes = dict()
    c = 0
    curr = head
    while curr:
        newnodes[c] = Node(curr.val)
        c+=1
        curr = curr.next
    
    for i in range(c):
        if i<c-1:
            newnodes[i].next = newnodes[i+1]
        if i in random: 
            newnodes[i].random = newnodes[random[i]]

    return newnodes[0] if len(newnodes)>0 else None


# how to use less memory:
# rather than hashing to index
# use 2 passes
# 1: make new nodes based on original list
# also hash old to new
# 2: use the hash to link new nodes to each other