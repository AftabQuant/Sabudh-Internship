class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicate_element(head):
    slow  = head
    fast = head.next
    while fast:
        if slow.data== fast.data: slow.next = fast.next
        else : slow = slow.next
        fast = fast.next
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
        print(head.data, end=" ")
        head = head.next
    print()

a = create_linked_list([11,11,11,13,13,20])
b = create_linked_list([10,15,15,15,20,20,20,23,25,25])
a = remove_duplicate_element(a)
b = remove_duplicate_element(b )
print_linkedlist(a)
print_linkedlist(b)