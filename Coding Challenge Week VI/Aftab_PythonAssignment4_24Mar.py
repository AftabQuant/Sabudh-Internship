class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_two_list(head1, head2):
    dummy = Node(-1)
    curr = dummy
    while head1 is not None and head2 is not None:
        if head1.data <= head2.data:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next
    if head1 is not None:
        curr.next = head1
    else:
        curr.next = head2
    return dummy.next

def merge_k_lists(arr):
    res = None
    for node in arr:
        res = merge_two_list(res, node)
    return res




