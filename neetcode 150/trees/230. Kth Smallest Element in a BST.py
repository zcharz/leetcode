from binarytree import *

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def helper(node):
            if not node: return []
            return helper(node.left) + [node.val] + helper(node.right)
        return helper(root)[k-1]


sol = Solution()
root = toBinaryTree([3,1,4,None,2])
k = 1
print(sol.kthSmallest(root, k))