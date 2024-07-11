from binarytree import *


from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        queue = deque()
        ret = []

        if root: queue.append(root)
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()                
                # if last element in layer (right most)
                if i == length-1: 
                    ret.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return  ret

sol = Solution()

root = toBinaryTree([1,2,3,None,5,None,4])
print(sol.rightSideView(root))

root = toBinaryTree([1,2])
print(toList(root))
print(sol.rightSideView(root))