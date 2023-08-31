class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def doubleIt(head: ListNode):
    if head and head.val == 0 and head.next == None:
        return head
    num = 0

    while head:
        num *= 10
        val = head.val
        num += val
        head = head.next
    
    num *= 2

    new_head = None


    while num > 0:
        val = num % 10
        num = num // 10
        new_node = ListNode(val)
        new_node.next = new_head
        new_head = new_node
    
    return new_head


