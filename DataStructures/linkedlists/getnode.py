#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
    size = 0
    cur = head
    while cur is not None:
        cur = cur.next
        size += 1
    size = size - 1 - position
    cur = head
    while size > 0:
        cur = cur.next
        size -= 1
    return cur.data