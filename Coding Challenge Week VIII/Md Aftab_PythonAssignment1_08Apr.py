class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def remove_greater(head):
    if head.next is None:
        return head
    dummy = ListNode(-1)
    temp = dummy
    prev = head
    cur = head.next
    while cur:
        if cur.val >= prev.val:
            prev = cur
            temp.next = cur
            cur = cur.next
            temp = temp.next
        else:
            prev = prev.next
            cur = cur.next
    return dummy.next

def print_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

if __name__ == "__main__":
    a = ListNode(5)
    b = ListNode(2)
    c = ListNode(13)
    d = ListNode(3)
    e = ListNode(8)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = None
    result = remove_greater(a)
    print_list(result)
