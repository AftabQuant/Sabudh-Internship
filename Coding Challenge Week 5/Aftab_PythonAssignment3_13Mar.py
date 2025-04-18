class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_two_linkedlist(h1, h2):
    if h1 is None and h2 is None: return None
    dummy = Node(-1)
    temp = dummy
    while h1 is not None and h2 is not None:
        if h1.data <= h2.data:
            temp.next = h1
            temp = h1
            h1 = h1.next
        else:
            temp.next = h2
            temp = h2
            h2 = h2.next
    while h1 is not None:
        temp.next = h1
        temp = h1
        h1 = h1.next
    while h2 is not None:
        temp.next = h2
        temp = h2
        h2 = h2.next
    return dummy.next

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
        print(head.data, end=", ")
        head = head.next
    print()

a = create_linked_list([1,2,4])
b = create_linked_list([1,3,4])
res = merge_two_linkedlist(a, b)
print_linkedlist(res)