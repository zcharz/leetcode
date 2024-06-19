from binarytree import *
import collections

# iterative in order traversal keeping max
# by definition next should be bigger than max 
def isValidBST(root: TreeNode) -> bool:
    stack = []
    curr = root
    val = None
    while stack or curr:
        # find all paths expanding strictly left first
        while curr:
            stack.append(curr)
            curr = curr.left
        # always last value added after initial 
        curr = stack.pop()

        if val!=None and not curr.val>val:
            return False
        val = curr.val
        curr = curr.right
    
    return True

# backtracking solution 
# updating the range the current node needs to be in each recursive call
# by changing one of the boundaries to the parent's value
# depending on which side it is recurring to
def isValidBST(root: TreeNode) -> bool:
    def valid(node, left, right):
        if not node:
            return True
        if not (left < node.val < right):
            return False

        return valid(node.left, left, node.val) and valid(node.right, node.val, right)

    return valid(root, float("-inf"), float("inf"))