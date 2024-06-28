from binarytree import *


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not q or not p or p.val != q.val: 
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)