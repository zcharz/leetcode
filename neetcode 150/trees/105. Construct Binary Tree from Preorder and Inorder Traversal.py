from binarytree import *

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if not preorder: return None
        left_inorder, right_inorder = inorder[:inorder.index(preorder[0])], inorder[inorder.index(preorder[0])+1:]
        left_preorder, right_preorder = preorder[1:len(left_inorder)+1], preorder[len(left_inorder)+1:]
        return TreeNode(preorder[0], self.buildTree(left_preorder, left_inorder), self.buildTree(right_preorder, right_inorder))

sol = Solution()

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
print(toList(sol.buildTree(preorder, inorder)))