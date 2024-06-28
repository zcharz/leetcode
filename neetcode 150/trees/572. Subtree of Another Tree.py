from binarytree import *

def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    def isSameTree(p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not q or not p or p.val != q.val: 
            return False
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    if subRoot == None:
        return True
    if root == None:
        return False
    
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot) or isSameTree(root, subRoot)


root = to_binary_tree([3,4,5,1,2,None,None,None,None,0])
subRoot = to_binary_tree([4,1,2])


print(isSubtree(root, subRoot))