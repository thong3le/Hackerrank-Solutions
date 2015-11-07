def HasCycle(head):
    count = 0
    cur = head
    while cur is not None and count <= 101:
        cur = cur.next
        count += 1
    if count > 100:
        return 1
    else:
        return 0