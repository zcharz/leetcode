from binarytree import *

import collections

# BFS 
# each time add the most right element to the return
def rightSideView(root: TreeNode) -> list[int]:
    if not root:
        return
    
    ret = []
    queue = collections.deque()
    queue.append(root)

    while queue:
        print()
        for node in queue:
            print(node.val, end=' ')
        
        c = len(queue)

        for i in range(c):
            node = queue.popleft()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            if i==c-1: ret.append(node.val)

    return ret


root = to_binary_tree([1,2,3,None,5,None,4])
print(rightSideView(root))