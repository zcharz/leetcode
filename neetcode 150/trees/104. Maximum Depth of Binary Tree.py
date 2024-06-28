from binarytree import *

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) +1

sol = Solution()
root = toBinaryTree([3,9,20,None,None,15,7])
print(sol.maxDepth(root))