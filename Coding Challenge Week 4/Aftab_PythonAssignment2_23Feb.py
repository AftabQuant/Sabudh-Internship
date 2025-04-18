class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_middle_linkedlist(head):
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    slow.next = slow.next.next
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

a = create_linked_list([1,2,3,4,5,6])
b = create_linked_list([2,4,6,7,5,1])
a = delete_middle_linkedlist(a)
b = delete_middle_linkedlist(b )
print_linkedlist(a)
print_linkedlist(b)