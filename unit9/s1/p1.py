# edge
#if not root:
# return None

from collections import deque 

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

class TreeNode():
     def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right

def merge_orders(order1, order2):
    # if value exists add to new tree
    if not order1:
        return order2
    if not order2:
        return order1
    sumNode = TreeNode(order1.val + order2.val)

    sumNode.left = merge_orders(order1.left, order2.left)
    sumNode.right = merge_orders(order1.right, order2.right)
    return sumNode
    




# """
#      1             2         
#     /  \         /   \       
#    3    2       1     3   
#  /               \      \   
# 5                 4      7   
# """
# Using build_tree() function included at top of page
cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

# Using print_tree() function included at top of page
# print_tree(merge_orders(order1, order2))

# Example Usage:

# [3, 4, 5, 5, 4, None, 7]
# Explanation:
# Merged Tree:
#      3
#     /  \      
#   4     5  
#  / \      \
# 5   4      7

# -0-----------------------------------------

class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(design):
    if not design:
        return
    
    q = deque([design])
    result = []

    while q:
        curr = q.popleft()
        result.append(curr.val)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
        # q.extend([curr.left, curr.right])

    # print(result)

    

# Example Usage:

# """
#             Vanilla
#            /       \
#       Chocolate   Strawberry
#       /     \
#   Vanilla   Matcha  
# """
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print_design(croquembouche)

# Example Output:

# ['Vanilla', 'Chocolate', 'Strawberry', 'Vanilla', 'Matcha']

# --------------------------------------------------
def max_tiers(cake):
    if cake is None:
        return 0
    
    # Process current node
    print(cake.val)
    leftHeight = max_tiers(cake.left)
    rightHeight = max_tiers(cake.right)
    return max(leftHeight,rightHeight) + 1
    
    

# Example Usage:

"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

print(max_tiers(cake))

# Example Output:

# 3
