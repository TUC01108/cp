from collections import deque


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def bfs_topView(root):
    if not root:
        return
    hd_map = {}
    queue = deque([(root, 0)])
    while queue:
        node, hd = queue.popleft()
        if hd not in hd_map:
            hd_map[hd] = node.info
        if node.left:
            queue.append((node.left,hd-1))
        if node.right:
            queue.append((node.right, hd+1))
    for hd in sorted(hd_map.keys()):
        print(hd_map[hd], end = " ")

    pass


# Manually define the binary tree
root = Node(1)
root.right = Node(2)
root.right.right = Node(5)
root.right.right.left = Node(3)
root.right.right.right = Node(6)
root.right.right.left.left = Node(4)

# Run it
bfs_topView(root)