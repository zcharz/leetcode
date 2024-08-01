from binarytree import *
from collections import deque

class Codec:

    def serialize(self, root):
        queue = deque([root])
        ret = []

        while queue:
            curr = queue.popleft()
            if curr:
                ret.append(str(curr.val))
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                ret.append('.')

        return ' '.join(ret)
        

    def deserialize(self, data):
        data = data.split(' ')
        data = deque(data)
        if not data or data[0] == '.': return None

        root = TreeNode(int(data[0]))
        data.popleft()
        nodes = deque([root])

        while nodes:
            curr = nodes.popleft()
            if not curr: continue

            leftval = data.popleft()
            rightval = data.popleft()

            if leftval != '.': 
                curr.left = TreeNode(int(leftval))
                nodes.append(curr.left)
            if rightval != '.': 
                curr.right = TreeNode(int(rightval))
                nodes.append(curr.right)

        return root
        

sol = Codec()

root = toBinaryTree([1,2,3,None,None,4,5])
serial = sol.serialize(root)
print(serial)
deserial = sol.deserialize(serial)
print(sol.serialize(deserial))

root = toBinaryTree([])
serial = sol.serialize(root)
print(serial)
deserial = sol.deserialize(serial)
print(sol.serialize(deserial))