from binarytree import * 


def diameterOfBinaryTree(root: TreeNode) -> int:
    def recur(root) -> (int, int):
        # height, furthest total

        if not root:
            #if root == None
            return 0, 0

        left = recur(root.left)
        right = recur(root.right)

        height = max(left[0], right[0])+1
        total = left[0]+right[0]

        return (height, max(total, left[1], right[1]))

    return recur(root)[1]



# neetcode solution
# modifying max from recursive function to original call


def diameterOfBinaryTree(root: TreeNode) -> int:
    res = 0

    def dfs(root):
        nonlocal res

        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)

        # update new max diameter
        res = max(res, left + right)

        return 1 + max(left, right)

    dfs(root)
    # dfs doesn't return but updates value instead
    return res