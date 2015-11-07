def RemoveDuplicates(head):
    d = set()
    if head is None:
        return head
    cur = head
    d.add(cur.data)
    while cur.next is not None:
        if cur.next.data in d:
            cur.next = cur.next.next
            if cur is None:
                return head 
        else:
            d.add(cur.next.data)
            cur = cur.next
            
    return head