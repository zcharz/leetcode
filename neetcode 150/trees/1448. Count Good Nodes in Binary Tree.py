from binarytree import *

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, maxtop)->int:
            if not node: return 0
            curr = 1 if node.val>=maxtop else 0
            return helper(node.left, max(node.val, maxtop)) + helper(node.right, max(node.val, maxtop)) + curr
        return helper(root, root.val)

sol = Solution()
root = toBinaryTree([3,1,4,3,None,1,5])
print(sol.goodNodes(root))