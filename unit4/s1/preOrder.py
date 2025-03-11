class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

# def insert(root, key):
#     if root is None:
#         return Node(key)
#     else:
#         if root.info < key:
#             root.right = insert(root.right, key)
#         else:
#             root.left = insert(root.left, key)
#     return root

def preOrder(root):
    #Write your code here
    if not root:
        return
    # stack = [root]
    # while stack:
        # node = stack.pop()
        # print(root.info, end =" ")
        # if node.right:
            # stack.append(node.right)
        # if node.left:
            # stack.append(node.left)
    print(root.info, end =" ")
    preOrder(root.left)
    preOrder(root.right) 


# # Construct the binary tree from the given sequence
# sequence = [1, 2, 5, 3, 6, 4]
# root = None
# for key in sequence:
#     root = insert(root, key)

# Manually define the binary tree
root = Node(1)
root.right = Node(2)
root.right.right = Node(5)
root.right.right.left = Node(3)
root.right.right.right = Node(6)
root.right.right.left.left = Node(4)

# Perform pre-order traversal
preOrder(root)