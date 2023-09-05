

def insertGreatestCommonDivisors(head):
    if not head.next:
        return head
    def findGCD(a, b):
        while b:
            a, b = b, a % b
        return a
    
    new_head = None
    ptr = None

    while head.next:
        print(head.val, ptr.val if ptr else None)
        first = head.val
        second = head.next.val

        min_v, max_v = min(first, second), max(first, second)

        gcd = findGCD(min_v, max_v)
        print("gcd", gcd)

        new_node_1 = ListNode(first)
        new_node_2 = ListNode(gcd)

        new_node_1.next = new_node_2

        if not new_head:
            new_head = new_node_1
            ptr = new_node_2
        else:
            ptr.next = new_node_1
            ptr = new_node_2
        
        head = head.next
    

    if head and ptr:
        ptr.next = ListNode(head.val)
    
    return new_head
        