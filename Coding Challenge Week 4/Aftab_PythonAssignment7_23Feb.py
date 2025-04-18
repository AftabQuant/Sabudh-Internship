class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_second_last(head):
    if not head or not head.next:
        return None
    while head.next.next:
        head = head.next
    return head.data

def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

list1 = create_linked_list([2, 4, 6, 8, 33, 67])
print(find_second_last(list1))

list2 = create_linked_list([1, 2, 3, 4, 5])
print(find_second_last(list2))
