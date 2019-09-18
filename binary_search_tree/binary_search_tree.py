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