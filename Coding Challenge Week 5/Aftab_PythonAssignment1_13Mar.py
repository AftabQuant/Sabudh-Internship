# Question 1.  Inserting at the Beginning
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_start(head, val):
    temp = Node(val)
    if head is None: head = temp
    else:
        temp.next = head
        head = temp
    return head

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

a = create_linked_list([2,3,4,5,6])
b = create_linked_list([3,2,5,7,1,2])
a = insert_at_start(a, 1)
b = insert_at_start(b,9 )
print_linkedlist(a)
print_linkedlist(b)
