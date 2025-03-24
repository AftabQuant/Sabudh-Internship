class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def add_two_numbers(l1, l2):
    dummy = Node(0)
    current = dummy
    carry = 0
    while l1 or l2 or carry:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        total = x + y + carry
        carry = total // 10
        current.next = Node(total % 10)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummy.next
