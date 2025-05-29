class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def delete_duplicates(head):
    temp = head
    while temp and temp.next:
        if temp.val == temp.next.val:
            temp.next = temp.next.next
        else:
            temp = temp.next
    return head