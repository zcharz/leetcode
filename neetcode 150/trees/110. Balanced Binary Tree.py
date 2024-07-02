from binarytree import *
import math

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(node):
            if not node:
                return 0, True
            
            left_height, left = helper(node.left)
            right_height, right = helper(node.right)

            height = max(left_height, right_height)+1
            con = True if left and right and math.abs(left_height, right_height)<2 else False
            return height, con
            # return max(left_height, right_height)+1, True if left and right and math.abs(left_height, right_height)<2 else False
        
        return helper(root)[1]


sol = Solution()


root = toBinaryTree([3,9,20,None,None,15,7])
print(sol.isBalanced(root))

root = toBinaryTree([1,2,2,3,None,None,3,4,None,None,4])
print(sol.isBalanced(root))

root = toBinaryTree([0])
print(sol.isBalanced(root))