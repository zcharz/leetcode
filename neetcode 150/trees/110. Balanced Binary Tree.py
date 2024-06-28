from binarytree import *


def isBalanced(root: TreeNode) -> bool:
    def recur(root):
        if root == None:
            return 0, True
        lefth, leftc = recur(root.left)
        righth, rightc = recur(root.right)

        if not (leftc and rightc):
            return 0, False

        balance = lefth-righth
        if not -1<=balance<=1:
            return 0, False
        return max(lefth, righth) +1, True

    return recur(root)[1]
    

# neetcode solution
# new funciton returns 2 values
# more concise code

def isBalanced(root: TreeNode) -> bool:
    def dfs(root):
        if not root:
            return [True, 0]

        left, right = dfs(root.left), dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return [balanced, 1 + max(left[1], right[1])]

    return dfs(root)[0]