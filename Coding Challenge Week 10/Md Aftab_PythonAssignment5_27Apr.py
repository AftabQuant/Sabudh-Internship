class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_before_middle(head, value):
    count = 0
    temp = head
    while temp:
        count += 1
        temp = temp.next

    middle_pos = (count // 2)
    new_node = Node(value)
    if middle_pos == 0:
        new_node.next = head
        return new_node

    temp = head
    for _ in range(middle_pos - 1):
        temp = temp.next
    new_node.next = temp.next
    temp.next = new_node

    return head

def print_list(head):
    while head:
        print(head.data, end="->" if head.next else "\n")
        head = head.next

nodes = [Node(i) for i in [1, 2, 3, 4, 5]]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]
head = nodes[0]

head = insert_before_middle(head, 9)

print_list(head)
