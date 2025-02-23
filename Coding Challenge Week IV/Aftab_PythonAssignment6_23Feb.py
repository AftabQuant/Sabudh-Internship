class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_list(head):
    prev, current = None, head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def add_two_lists(head1, head2):
    head1 = reverse_list(head1)
    head2 = reverse_list(head2)
    carry = 0
    dummy = Node(0)
    current = dummy
    while head1 or head2 or carry:
        sum_val = carry
        if head1:
            sum_val += head1.data
            head1 = head1.next
        if head2:
            sum_val += head2.data
            head2 = head2.next
        carry, value = divmod(sum_val, 10)
        current.next = Node(value)
        current = current.next
    return reverse_list(dummy.next)

def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end="->")
        head = head.next
    print("NULL")

a = create_linked_list([5, 6, 3])
b = create_linked_list([8, 4, 2])
result = add_two_lists(a, b)
print_linked_list(result)

c = create_linked_list([7, 5, 9, 4, 6])
d = create_linked_list([8, 4])
result2 = add_two_lists(c, d)
print_linked_list(result2)
