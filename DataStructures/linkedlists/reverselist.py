"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    if head is None:
        return head
    newhead = Node(head.data, None)
    head = head.next
    while head is not None:
        node = Node(head.data, newhead)
        newhead = node
        head = head.next
    return newhead