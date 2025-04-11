from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right
def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

         
def count_odd_splits(root):
    if not root:
        return 0
count = 0
def traverse(node):
    global count
    if node:
        traverse(node.left)
        if node.val %2 != 0:
            count += 1
        traverse(node.right)
    return count

# Example Usage:

# """
#       2
#      / \
#     /   \
#    3     5
#   / \     \
#  6   7     12
# """

# Using build_tree() function included at top of page
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(traverse(monstera))
print(count_odd_splits(None))




found = False
def find_flower(node, name):
    global found
    if node:
        find_flower(node.left, name)
        if node.val == name:
            found = True
            return found
        find_flower(node.right, name)
    return found

# Example Usage:

# """
#           Rose
#          /    \
#       Lilac  Tulip
#       /  \       \
#    Daisy Lily   Violet
# """

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 

# Example Output:

# True
# False




def add_plant(collection, name):
    if not collection:
        return TreeNode(name)
    
    # if name not in tree find left most subtree and insert
    # if value  == name
    # add new node to existing node's right subtree 
    if name < collection.val:
        collection.left = add_plant(collection.left, name)
    elif name > collection.val:
        collection.right = add_plant(collection.right, name)
    
    return collection



# Example Usage:

# """
#             Money Tree
#         /              \
# Fiddle Leaf Fig    Snake Plant
# """

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Aloe"))

# Example Output:

# ['Money Tree', 'Fiddle Leaf Fig', 'Snake Plant', 'Aloe']

# Explanation: 
# Tree should have the following structure:
#            Money Tree
#         /              \
#  Fiddle Leaf Fig   Snake Plant
#    /
#  Aloe


