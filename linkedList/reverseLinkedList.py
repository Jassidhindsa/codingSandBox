
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head):
    linkedList = None

    while head:
        print(head.val)
        new_node = ListNode(head.val)
        new_node.next = linkedList
        linkedList = new_node
        head = head.next
    
    return linkedList
    

if __name__ == "__main__":
    linkedList = None
    linkedListHead = None
    nums = [1,2,3,4,5]

    for num in nums:
        new_node = ListNode(num)
        if not linkedListHead:
            linkedListHead = new_node
        linkedList = new_node
        linkedList = linkedList.next
    output = reverseLinkedList(linkedListHead)

    while output:
        print(output.val)
        output = output.next
