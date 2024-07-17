from binarytree import *


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        # checking layer by layer up
        def helper(node):
            # returns validity, min, max
            if not node.left and not node.right:
                return (True, node.val, node.val)
            elif node.left and not node.right:
                left, leftmin, leftmax = helper(node.left)
                return (left and leftmax<node.val), leftmin, node.val
            elif node.right and not node.left:
                right, rightmin, rightmax = helper(node.right)
                return (right and node.val<rightmin), node.val, rightmax

            left, leftmin, leftmax = helper(node.left)
            right, rightmin, rightmax = helper(node.right)
            return (left and right and leftmax<node.val<rightmin), leftmin, rightmax
        
        return helper(root)[0]

    # checking layer by layer down
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, left, right):
            if not node: return True
            return left<node.val<right and helper(node.left, left, node.val) and helper(node.right, node.val, right)
        return helper(root, float('-inf'), float('inf'))

sol = Solution()

root = toBinaryTree([2,1,3])
print(sol.isValidBST(root))

root = toBinaryTree([5,1,4,None,None,3,6])
print(sol.isValidBST(root))