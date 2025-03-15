from collections import deque


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

root = Node(1)
root.right = Node(2)
root.right.right = Node(5)
root.right.left = Node(7)
root.right.right.left = Node(3)
root.right.right.right = Node(6)
root.right.right.left.left = Node(4)

def levelOrder(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.info, end = " ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    pass

levelOrder(root)