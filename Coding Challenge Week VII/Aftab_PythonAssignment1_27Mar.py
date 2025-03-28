class Node :
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse(head) :
    if head is None or head.next is None: return head;
    new_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return new_head

def reverse_linkedlist(head, left, right) :
    if head.next is None : return head
    temp = head
    a , b, c, d = None, None, None, None
    pos = 1
    while temp is not None:
        if pos == left-1: a = temp
        if pos == left: b = temp
        if pos == right: c = temp
        if pos == right+1: d = temp
        temp = temp.next
        pos += 1
    if a: a.next = None
    if c: c.next = None
    new_head = reverse(b)
    if a is not None: a.next = new_head
    temp = new_head
    while temp and temp.next:
        temp = temp.next
    if temp:
        temp.next = d
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
        print(head.val, end=" ")
        head = head.next
    print()

a = create_linked_list([1,2,3,4,5])
res1 = reverse_linkedlist(a,2,4)
print_linkedlist(res1)

b = create_linked_list([5])
res2 = reverse_linkedlist(b, 1, 1)
print_linkedlist(res2)