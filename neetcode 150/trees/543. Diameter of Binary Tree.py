from binarytree import * 

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # using global variable
        diameter = [0]

        def helper(node):
            if not node:
                return 0
            left_height = helper(node.left)
            right_height = helper(node.right)
            diameter[0] = max(left_height+right_height, diameter[0])
            return max(left_height, right_height)+1

        helper(root)
        return diameter[0]


        # passing up current max diameter
        def helper(node):
            if not node: 
                return 0, 0

            left = helper(node.left)
            right = helper(node.right)
            return max(left[0], right[0])+1, max(left[1], right[1], left[0]+right[0])

        return helper(root)[1]

sol = Solution()

root = toBinaryTree([1,2,3,4,5])
print(sol.diameterOfBinaryTree(root))

root = toBinaryTree([1,2])
print(sol.diameterOfBinaryTree(root))