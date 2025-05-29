class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linkedlist(head):
    if head is None or head.next is None: return head
    new_head = reverse_linkedlist(head.next)
    head.next.next = head
    head.next = None
    return new_head

def create_linked_list(arr):
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
        print(head.data, end="->")
        head = head.next
    print()

a = create_linked_list([1,2,3,4])
b = create_linked_list([1,2,3,4,5])
a = reverse_linkedlist(a)
b = reverse_linkedlist(b )
print_linkedlist(a)
print_linkedlist(b)