class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def middle_of_linkedlist(head):
    slow = fast = head
    while fast and fast.next :
        slow = slow.next
        fast = fast.next.next
    return slow.data

