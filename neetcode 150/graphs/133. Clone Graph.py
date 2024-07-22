# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        oldtonew = dict()
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr not in oldtonew:
                oldtonew[curr] = Node(curr.val)
                stack.extend(curr.neighbors)

        for old, new in oldtonew.items():
            for neighbor in old.neighbors:
                new.neighbors.append(oldtonew[neighbor])

        return oldtonew[node]