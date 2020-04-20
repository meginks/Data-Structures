from doubly_linked_list import DoublyLinkedList
# What has already been provided for me?
# What do I need to use that's not already there?
# What do I need to return/what do I need to end up with?
"""
Our LRUCache class keeps track of the max number of nodes it
can hold,
 the current number of nodes it is holding,
 a doubly-
linked list that holds the key-value entries in the correct 
order,
as well as a storage dict that provides fast access
to every node stored in the cache.
""" 
class LRUCache:
  def __init__(self, limit=10):
    self.limit = limit
    self.current_size = 0
    self.order = DoublyLinkedList()
    self.fast_access = {}
  def search_and_if_exists_move_to_front(self, key):
    found = False
    current = self.order.head
    while current:
      if current.value == key:
        # If we're updating, then move that key to be the most recent key (move it to the head)
        self.order.move_to_front(current)
        found = True
      current = current.next
    if not found:
      # Add key and value to the ordered list, and we're going to keep the most recent value at the head, or the beginning of the list
      self.order.add_to_head(key)
      self.current_size += 1
  """
  Retrieves the value associated with the given key.
  
  Also needs to move the key-value pair to the top of the order such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    # Check the cache to see if it exists
    if key in self.fast_access:
      # If it exists, move it to the front in the order and return the value
      self.search_and_if_exists_move_to_front(key)
      return self.fast_access[key]
    # If it doesn't exist
    else:
      return None
  """
  Adds the given key-value pair to the cache.
  
  The newly-
  added pair should be considered the most-recently used
  entry in the cache.
  
  If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room.
  
  Additionally, in the case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  # LRUCache.set(0, 23)
  # LRUCache.set(0, 567)
  def set(self, key, value):
    # If it's not full
    if self.current_size < self.limit:
      # Add key and value to the fast_access dictionary or update if it already exists
      self.fast_access.update({key: value})
      # What if the value already exists?
      # Loop through the ordered list, and if we find that the key is already there, update the value and move to the top of the list
      self.search_and_if_exists_move_to_front(key)
    # If it's full
    else:
      self.fast_access.update({key: value})
      # Look for the key to see whether or not it already exists
      found = False
      current = self.order.head
      while current:
        if current.value == key:
          # If we're updating, then move that key to be the most recent key (move it to the head)
          self.order.move_to_front(current)
          found = True
        current = current.next
      # If the key was not already in our cache
      if not found:
         key_to_remove = self.order.remove_from_tail()
         print("key_to_remove", key_to_remove)
         self.fast_access.pop(key_to_remove)
         # Set the new item in the ordered list (it already exists in the cache because we updated at the very beginning)
         self.order.add_to_head(key)
         self.current_size += 1
      # If the key doesn't already exists, put it at the front
