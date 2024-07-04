from binarytree import *

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if (not p or not q) or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
sol = Solution()
p = toBinaryTree([1,2,3])
q = toBinaryTree([1,2,3])
print(sol.isSameTree(p, q))