# single-linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# double_linked list
class DoubleListNode(object):
    """
    A more specific implement for double-linked list is shown in recommend order-9: 707 Design Linked List
    """
    def __init__(self, x):
        self.val = x
        self.pre = None
        self.next = None
