class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 
    
def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.
        if not self.root:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                # if val < self insert somewhere to left
                if val < current.info:
                    if current.left is None:
                        current.left = Node(val)
                        break
                    else:
                        current = current.left
                # if val > self insert somewhere on right
                if val > current.info:
                    if current.right is None:
                        current.right = Node(val)
                        break
                    else: 
                        current = current.right

# Create an instance of BinarySearchTree
tree = BinarySearchTree()

# Manually define the binary tree by inserting nodes
tree.insert(4)
tree.insert(2)
tree.insert(7)
tree.insert(1)
tree.insert(3)

# Insert the value 6
tree.insert(6)

# Print the tree using preOrder traversal
preOrder(tree.root)
