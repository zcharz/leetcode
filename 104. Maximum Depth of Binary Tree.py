from binarytree import *

def maxDepth(root: TreeNode) -> int:
    if root:
        return max(maxDepth(root.left), maxDepth(root.right)) + 1
    return 0