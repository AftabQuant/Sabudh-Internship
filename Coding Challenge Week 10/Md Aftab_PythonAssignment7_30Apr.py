class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def rotate_right(head, k):
    if not head or k == 0:
        return head

    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
    k = k % length
    if k == 0:
        return head
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    tail.next = head
    return new_head

def print_list(head):
    while head:
        print(head.data, end="->" if head.next else "\n")
        head = head.next

def create_linked_list(values):
    if not values:
        return None
    nodes = [Node(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]

head1 = create_linked_list([10, 20, 30, 40, 50, 60])
k1 = 4
head1 = rotate_right(head1, k1)
print_list(head1)

head2 = create_linked_list([30, 40, 50, 60])
k2 = 2
head2 = rotate_right(head2, k2)
print_list(head2)
