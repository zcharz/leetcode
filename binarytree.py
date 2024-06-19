from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# doesnt work with skipped Nones
def to_binary_tree(items: list[int]) -> TreeNode:
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


def tree_to_list(root):
    ret = []
    queue = deque()
    queue.append(root)
    while queue:
        for i in range(len(queue)):
            curr = queue.popleft()
            if curr!=None:
                queue.append(curr.left)
                queue.append(curr.right)
                ret.append(curr.val)
            else:
                ret.append(None)
    return ret

