from binarytree import *

# assume n>k
# worst case O(n) time, O(n) space for recursive stack


# doesn't work but is close enough
# leetcode buggy????
def kthSmallest(root: TreeNode, k: int) -> int:
    def dfs(node, c):
        if not node:
            return 0, None
            
        left_c, left_ret = dfs(node.left, c)
        if left_ret:
            return left_c, left_ret
        
        c+=left_c
        c+=1
        
        if c==k:
            return c, node.val

        right_c, right_ret = dfs(node.right, c)
        if right_ret:
            return right_c, right_ret
        
        return c+right_c, None
    
    return dfs(root, 0)[1]


# iterative solution
def kthSmallest(root: TreeNode, k: int) -> int:
    stack = []
    curr = root

    while stack or curr:
        # follow left side of tree, add all nodes
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        k-=1
        if k == 0:
            return curr.val
        curr = curr.right


test = [3,1,4,None,2]
root = to_binary_tree(test)
print(kthSmallest(root,3))