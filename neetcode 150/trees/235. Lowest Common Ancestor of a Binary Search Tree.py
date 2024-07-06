from binarytree import *

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val<root.val and q.val<root.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

        # iterative solution
        while True:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root

sol = Solution()

root = toBinaryTree([6,2,8,0,4,7,9,None,None,3,5])
p = toBinaryTree([2])
q = toBinaryTree([8])
print(sol.lowestCommonAncestor(root, p, q).val)

root = toBinaryTree([6,2,8,0,4,7,9,None,None,3,5])
p = toBinaryTree([2])
q = toBinaryTree([4])
print(sol.lowestCommonAncestor(root, p, q).val)