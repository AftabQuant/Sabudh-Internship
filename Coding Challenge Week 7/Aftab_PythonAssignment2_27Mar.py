class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def odd_even_linkedlist(head):
    if not head or not head.next:
        return head
    odd = head
    even = head.next
    even_head = even
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head

def create_linkedlist(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

def print_linkedlist(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

ar = create_linkedlist([1, 2, 3, 4, 5])
res = odd_even_linkedlist(ar)
print_linkedlist(res)

br = create_linkedlist([2,1,3,5,6,4,7])
res = odd_even_linkedlist(br)
print_linkedlist(res)