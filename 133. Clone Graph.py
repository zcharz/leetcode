class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


import collections

def cloneGraph(node: 'Node') -> 'Node':
    if not Node:
        return 

    seen = set()

    nodes = dict()
    neigh = dict()

    queue = collections.deque()
    queue.append(node)

    # create each node without assigning to their neighbor
    # each node is mapped to their value in dict nodes
    while queue:
        curr = queue.popleft()
        if not curr:
            continue

        nodes[curr.val] = Node(curr.val)

        neigh[curr.val] = [n.val for n in curr.neighbors]
        seen.add(curr.val)

        for n in curr.neighbors:
            if n and n.val not in seen:
                queue.append(n)
                seen.add(n.val)

        # queue.extend([n for n in curr.neighbors if n.val not in seen])

    # assign neighbors
    for n in nodes.values():
        n.neighbors = [nodes[i] for i in neigh[n.val]]

    return nodes[1]


# test
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]


new = cloneGraph(n1)
seen = set()
neigh = dict()

queue = collections.deque()
queue.append(new)


while queue:
    curr = queue.popleft()

    neigh[curr.val] = [n.val for n in curr.neighbors]
    seen.add(curr.val)

    for n in curr.neighbors:
        if n.val not in seen:
            queue.append(n)
            seen.add(n.val)

print(neigh)



# neetcode backtracking solution
# use a hashmap to map original to new copy
# DFS or BFS through from start to entire graph
# if clone exists, attach it
# if clone doesn't exist, recursively clone it
# O(N) time 

def cloneGraph(node: 'Node') -> 'Node':
    hashmap = dict()

    def dfs(node):
        # if old exists as a key
        if node in hashmap:
            return hashmap[node]
        
        # now it doesnt exist, must copy
        copy = Node(node.val)
        hashmap[node] = copy
        for neighbor in node.neighbors:
            # this will recursively return a copy of each neighbor
            # no need for "seen" 
            # since hashmap acts as seen
            copy.neighbors.append(dfs(neighbor))
        # at this point the neighbors must have their correct neighbors already
        return copy

    # edge case if node is None
    return dfs(node) if node else None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

# in this test the backtracking solution will
# make 1, make 2, make 3, make 4
# then since both 4s neighbors exists
# add 1 and 3 to 4
# backtrack to 4
# add 2 and 4 to 3
# backtrack to 2
# add 1 and 3 to 2
# backtrack to 1
# add 2 and 3 to 1