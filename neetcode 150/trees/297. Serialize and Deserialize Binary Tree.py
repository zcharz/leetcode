from binarytree import *
from collections import deque

class Codec:
    def serialize(self, root):
        ret = []
        
        def dfs(node):
            if not node:
                ret.append('N')
                return 
            
            ret.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ','.join(ret)


    def deserialize(self, data):
        pos = [0]
        data = data.split(',')

        def recur():
            if data[pos[0]]=='N':
                pos[0]+=1
                return None

            curr = TreeNode(data[pos[0]])
            pos[0]+=1
            curr.left = recur()
            curr.right = recur()
            return curr
        
        
            
        return recur()
    
    # level order traversal
    # doesnt with with gaps of Nones
    # def serialize(self, root):
    #     ret = ''
    #     queue = deque()
    #     queue.append(root)
    #     while queue:
    #         for i in range(len(queue)):
    #             curr = queue.popleft()
    #             if curr:
    #                 queue.append(curr.left)
    #                 queue.append(curr.right)
    #                 ret+=str(curr.val)
    #             else:
    #                 ret+=' '
    #     return ret
    
    # def deserialize(self, data):
    #     def recur(c):
    #         if c<len(data)+1 and data[c-1]!='N':
    #             return TreeNode(int(data[c-1]), recur(c*2), recur(c*2+1) )
    #         return None
    #     return recur(-1)


ser = Codec()
deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

li = [1,2,3,None,None,4,5]
# li = [1,2,3,None,None,4,5,6,7]
root = to_binary_tree(li)
string = ser.serialize(root)
print(string)

ans = deser.deserialize(string)
print(tree_to_list(ans))
