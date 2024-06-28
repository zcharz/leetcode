from binarytree import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left)) if root else None
        if not root:
            return None

        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        return root

sol = Solution()

root = [4,2,7,1,3,6,9]
binary_tree = toBinaryTree(root)
print(toList(binary_tree))
print(toList(sol.invertTree(binary_tree)))


root = [2,1,3]
binary_tree = toBinaryTree(root)
print(toList(binary_tree))
print(toList(sol.invertTree(binary_tree)))
