from binarytree import *

# preorder traversal
def goodNodes(root: TreeNode) -> int:
    def helper(node, val):
        if not node:
            return 0
        c = 1 if not node.val<val else 0
        return c+helper(node.left, max(val,node.val))+helper(node.right, max(val,node.val))
    return helper(root, root.val)