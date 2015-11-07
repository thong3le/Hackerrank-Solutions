"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def MergeLists(headA, headB):
    curA = headA
    curB = headB
    cur = curA
    if headA is None:
        return headB
    if headB is None:
        return headA
    if headA.data <= headB.data:
        head = headA
        curA = curA.next
    else:
        head = headB
        cur = curB
        curB = curB.next
        
    while curA is not None and curB is not None:
        if curA.data <= curB.data:
            cur.next = curA
            curA = curA.next
        else:
            cur.next = curB
            curB = curB.next
        cur = cur.next
    while curA is not None:
        cur.next = curA
        curA = curA.next
        cur = cur.next
    while curB is not None:
        cur.next = curB
        curB = curB.next
        cur = cur.next
  
    return head