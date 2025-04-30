class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_last_occurrence(head, key):
    last = None
    last_prev = None
    prev = None
    curr = head
    while curr:
        if curr.data == key:
            last = curr
            last_prev = prev
        prev = curr
        curr = curr.next
    if last is None:
        return head
    if last_prev is None:
        head = head.next
    else:
        last_prev.next = last.next
    return head

def print_list(head):
    while head:
        print(head.data, end="  -->  " if head.next else "NULL\n")
        head = head.next

def create_linked_list(values):
    if not values:
        return None
    nodes = [Node(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]

head1 = create_linked_list([1, 2, 3, 4, 5, 4, 4])
print("Created Linked list:", end=" ")
print_list(head1)
head1 = delete_last_occurrence(head1, 4)
print("List after deletion of 4:", end=" ")
print_list(head1)
print()

head2 = create_linked_list([11, 32, 123, 344, 445, 484, 534])
print("Created Linked list:", end=" ")
print_list(head2)
head2 = delete_last_occurrence(head2, 445)
print("List after deletion of 445:", end=" ")
print_list(head2)
