class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def postorder_iterative(root):
    if not root:
        return
    stack = []
    last_visited = None
    current = root
    
    while stack or current:
        # Push all left nodes to stack
        while current:
            stack.append(current)
            current = current.left
        
        # Peek at the top node
        node = stack[-1]
        
        # If no right child or right child was just visited, process this node
        if not node.right or node.right == last_visited:
            stack.pop()  # Remove node
            print(node.info, end=" ")  # Visit it
            last_visited = node  # Mark as visited
        else:
            current = node.right  # Explore right subtree
    
# Manually define the binary tree
root = Node(1)
root.right = Node(2)
root.right.right = Node(5)
root.right.right.left = Node(3)
root.right.right.right = Node(6)
root.right.right.left.left = Node(4)

# Run it
postorder_iterative(root)
# Output: 4 5 2 3 1
print()
def postorder_recursive(root):
    if not root:  # Base case: off the track
        return
    postorder_recursive(root.left)   # Left subtree
    postorder_recursive(root.right)  # Right subtree
    print(root.info, end=" ")         # Root last

# Run it
postorder_recursive(root)
# Output: 4 5 2 3 1