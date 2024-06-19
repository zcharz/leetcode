from binarytree import *

def buildTree(preorder: list[int], inorder: list[int]) -> TreeNode:
    if not preorder:
        return None
    
    leftin = inorder[:inorder.index(preorder[0])]
    rightin = inorder[inorder.index(preorder[0])+1:]

    leftpre = preorder[1:len(leftin)+1] 
    rightpre = preorder[len(leftin)+1:]

    node = TreeNode(preorder[0], 
                    buildTree( leftpre , leftin), 
                    buildTree( rightpre, rightin)  )

    return node

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

print(buildTree(preorder, inorder))

# while preorder:
#     leftin = inorder[:inorder.index(preorder[0])]
#     leftpre = preorder[1:len(leftin)+1] 

#     print(leftin, leftpre)
#     preorder = leftpre
#     inorder = leftin