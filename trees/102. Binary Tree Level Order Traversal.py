from binarytree import *


# BFS with queue like structure
# O(N) time and space complexity)


def levelOrder(root: TreeNode) -> list[list[int]]:    
    ret = []
    curr = [root]

    def childrenOf(list):
        l = []
        for node in list:
            if not node:
                continue

            if node.left!= None:
                l.append(node.left)
            if node.right!=None:
                l.append(node.right)
        return l
    
    # while curr not empty, there are more nodes/deeper layers left
    while curr: 
        vals = []
        for node in curr:
            # if node != None
            if node:
                vals.append(node.val)

        # if vals is non-empty
        if vals:
            ret.append(vals)

        curr = childrenOf(curr)
    return ret



# neetcode solution
# using collections.deque (double ended queue)

import collections

def levelOrder(root: TreeNode) -> list[list[int]]:
    res = []
    q = collections.deque()
    if root:
        q.append(root)

    while q:
        val = []

        for i in range(len(q)):
            node = q.popleft()
            val.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(val)
    return res