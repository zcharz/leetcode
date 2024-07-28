from binarytree import *


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(node):
            if not node: return float('-inf'), float('-inf')

            leftpath, leftmax = helper(node.left)
            rightpath, rightmax = helper(node.right)

            currpath = max(node.val+leftpath, node.val+rightpath, node.val)
            currmax = max(leftmax, rightmax, node.val+leftpath+rightpath, currpath)
            return currpath, currmax

        return helper(root)[1]



sol = Solution()

root = toBinaryTree([1,2,3])
print(sol.maxPathSum(root))

root = toBinaryTree([-10,9,20,None,None,15,7])
print(sol.maxPathSum(root))