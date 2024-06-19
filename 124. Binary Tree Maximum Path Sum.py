from binarytree import *

# at each intersection, you can:
# go left to middle to right
# forefit one side and go middle and up

def maxPathSum(root: TreeNode) -> int:
    def dfs(node):
        if not node:
            return None, 0
        
        left_total, left_incl = dfs(node.left)
        right_total, right_incl = dfs(node.right)
        left_incl = max(left_incl, 0)
        right_incl = max(right_incl, 0)

        if left_total!=None and right_total!=None:
            return max(node.val+left_incl+right_incl, left_total, right_total), node.val+max(left_incl, right_incl)
        elif left_total!=None:
            return max(node.val+left_incl, left_total), node.val+max(left_incl, right_incl)
        elif right_total!=None:
            return max(node.val+right_incl, right_total), node.val+max(left_incl, right_incl)
        return node.val, node.val+max(left_incl, right_incl)

    return dfs(root)[0]


# li = [-10,9,20,None,None,15,7]
li = [1,2,3]
# li = [-3]
# li = [1,2]
# li = [-1,5,None,4,None,None,2,-4]
root = to_binary_tree(li)
print(maxPathSum(root))


# neetcode solution
def maxPathSum(root: TreeNode) -> int:
    res = [root.val]    

    # return max path sum without split
    def dfs(root):
        if not root:
            return 0

        leftMax = dfs(root.left)
        rightMax = dfs(root.right)
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        # compute max path sum WITH split
        res[0] = max(res[0], root.val + leftMax + rightMax)
        return root.val + max(leftMax, rightMax)

    dfs(root)
    return res[0]