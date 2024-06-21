from binarytree import *

def lowestCommonAncestor(root, p, q):    
    if root.val==p.val or root.val==q.val or p.val<root.val<q.val or q.val<root.val<p.val:
        return root
    elif p.val<root.val:
        return lowestCommonAncestor(root.left, p, q)
    else:
        return lowestCommonAncestor(root.right, p, q)



test1 = to_binary_tree([6,2,8,0,4,7,9,None,None,3,5])
test2 = to_binary_tree([2,1])


print(lowestCommonAncestor(test1, TreeNode(2), TreeNode(8)).val)
print(lowestCommonAncestor(test1, TreeNode(2), TreeNode(4)).val)
print(lowestCommonAncestor(test2, TreeNode(2), TreeNode(1)).val)


# neetcode iterative solution
def lowestCommonAncestor(root, p, q):    
    while True:
        if root.val < p.val and root.val < q.val:
            root = root.right
        elif root.val > p.val and root.val > q.val:
            root = root.left
        else:
            return root