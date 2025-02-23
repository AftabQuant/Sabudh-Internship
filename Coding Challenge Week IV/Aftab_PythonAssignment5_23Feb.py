class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def add_one_util(head):
    if not head: return 1
    carry = add_one_util(head.next)
    sum_val = head.data + carry
    head.data = sum_val % 10
    return sum_val // 10

def add_one(head):
    carry = add_one_util(head)
    if carry:
        new_head = Node(carry)
        new_head.next = head
        head = new_head

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

def print_linked_list(head):
    while head:
        print(head.data, end="->")
        head = head.next
    print("NULL")


arr1 = [1, 9, 9, 9]
arr2 = [3, 4, 5, 3]

a = create_linked_list(arr1)
b = create_linked_list(arr2)

a = add_one(a)
b = add_one(b)

print_linked_list(a)
print_linked_list(b)
