import sys
sys.path.append('../queue_and_stack')
from queue import Queue
from stack import Stack

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value: 
      if not self.left: 
        self.left = BinarySearchTree(value)
      else: 
        self.left.insert(value)
    else: 
      if not self.right: 
        self.right = BinarySearchTree(value)
      else: 
        self.right.insert(value)

  def contains(self, target):
    if self.value == target: 
      return True
    elif target < self.value: 
      if self.left: 
        return self.left.contains(target)
    else: 
      if self.right: 
        return self.right.contains(target)
    return False

  def get_max(self):
    if not self.right: 
      return self.value  # base case for the get_max function because the left will always have the lower number in a binary tree. right will always be higher
    else: 
      return self.right.get_max() 

  def for_each(self, cb):
    cb(self.value) 
    if self.left: 
      self.left.for_each(cb)
    if self.right: 
      self.right.for_each(cb)

  def in_order_print(self, node):
    """ Use a recursive, depth first traversal  """
    if node is None: 
      return 
    self.in_order_print(node.left)
    print(node.value) 
    self.in_order_print(node.right)

  def bft_print(self, node):
    """ Print the value of every node, starting with the given node, use an iterative breadth first traversal """
    holding_cell = [] 
    traversal_queue = Queue() 
    while len(traversal_queue) > 0: 
            node = traversal_queue.dequeue() 
            holding_cell.append(node.value)
            if node.left_child: 
                traversal_queue.append(node.left_child) 
            if node.right_child: 
                traversal_queue.append(node.right_child) 
            holding_cell  
          
    
      
    
  def dft_print(self, node):
    """Print the value of every node, starting with the given node, in an iterative depth first traversal """
    holding_cell = []
    if node is None:
      return 
    # PREORDER 
    holding_cell.append(node.value)
    while node.left: 
      if node.left: 
        node = node.left 
        holding_cell.append(node.value)
    while node.right: 
      if node.right:
        node = node.right 
        holding_cell.append(node.value) 
    for node in holding_cell: 
      print(node)
    
    

# STRETCH-
    # Note: Research may be required
  def pre_order_dft(self, node):
    """Print Pre-order recursive DFT"""
    current_node = node 
    if current_node is None: 
      return 
    print(current_node.value) 
    self.pre_order_dft(current_node.left)
    self.pre_order_dft(current_node.right) 

    
  def post_order_dft(self, node):
    """Print Post-order recursive DFT""" 
    current_node = node
    if current_node is None: 
      return 
    self.post_order_dft(current_node.left)
    self.post_order_dft(current_node.right) 
    print(current_node.value) 
    
