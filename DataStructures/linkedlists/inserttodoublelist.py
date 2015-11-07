"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def SortedInsert(head, data):
    if head is None:
        return Node(data, None, None)
    if data <= head.data:
        node = Node(data, head, None)
        head.prev = node
        head = node
        return head
    
    cur = head
    while cur.next is not None and cur.data < data:
        cur = cur.next
        
    if cur.data <= data:
        node = Node(data, cur, None)
        cur.next = node
    else:
        node = Node(data, cur, cur.prev)
        cur.prev.next = node
        cur.prev = node
    
    return head