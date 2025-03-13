# Question 2.  Maximum Twin Sum of A Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linkedlist(head):
    if head is None or head.next is None: return head
    newhead = reverse_linkedlist(head.next)
    head.next.next = head
    head.next = None
    return newhead

def maximum_twin_sum(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    h1 = head
    h2 = reverse_linkedlist(slow)
    total = 0
    while h2:
        total = max(total, h1.data+h2.data)
        h1 = h1.next
        h2 = h2.next
    return total

def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

a = create_linked_list([1,2,4,5])
print(f"The maximum twin sum is: {maximum_twin_sum(a)}")
