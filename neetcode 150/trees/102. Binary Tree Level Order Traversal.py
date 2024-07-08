from binarytree import *
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        layer = deque([root])
        ret = []

        while layer:
            new_layer = deque()
            layer_out = []
            for node in layer:
                if not node:
                    continue

                layer_out.append(node.val)
                new_layer.append(node.left)
                new_layer.append(node.right)
            layer = new_layer
            if layer_out: ret.append(layer_out)

        return ret
    
sol = Solution()

root = toBinaryTree([3,9,20,None,None,15,7])
print(sol.levelOrder(root))

root = toBinaryTree([1])
print(sol.levelOrder(root))

root = toBinaryTree([])
print(sol.levelOrder(root))