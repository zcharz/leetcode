from binarytree import *


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def isSameTree(tree1, tree2):
            if not tree1 and not tree2:
                return True
            if not tree1 or not tree2 or tree1.val != tree2.val:
                return False
            return isSameTree(tree1.left, tree2.left) and isSameTree(tree1.right, tree2.right)
        
        if root: 
            return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 
        return isSameTree(root, subRoot)


sol = Solution()

root = toBinaryTree( [3,4,5,1,2])
subRoot = toBinaryTree([4,1,2])
print(sol.isSubtree(root, subRoot))

root = toBinaryTree([3,4,5,1,2,None,None,None,None,0])
subRoot = toBinaryTree([4,1,2])
print(sol.isSubtree(root, subRoot))