from collections import deque
from binarytree import *

# using heap like order of nodes, where root = 1, second layer = 2,3, third layer = 4, 5, 6, 7
# each child is calculated as the parent*2 and parent*2 + 1
# width = first node and last node in the queue


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = deque([(root, 1)])
        ret = 0
        while queue:
            ret = max(ret, queue[-1][1]-queue[0][1]+1)
            for i in range(len(queue)):
                curr, val = queue.popleft()
                if not curr: continue
                if curr.left: queue.append((curr.left, val*2))
                if curr.right: queue.append((curr.right, val*2+1))
        return ret
    

sol = Solution()

root = toBinaryTree([1,3,2,5,3,None,9])
print(sol.widthOfBinaryTree(root))

root = toBinaryTree([1,3,2,5])
print(sol.widthOfBinaryTree(root))
