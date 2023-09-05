class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):
        old_new_map, waiting_nodes = {}, {}

        new_head, ptr = None, None

        while head:
            val = head.val
            random = head.random
            new_node = Node(val)
            old_new_map[head] = new_node
            
            if not new_head:
                new_head = new_node
                ptr = new_node
            else:
                ptr.next = new_node
            
            ptr = new_node

            if head in waiting_nodes:
                for node in waiting_nodes[head]:
                    node.random = ptr
                del waiting_nodes[head]
            
            if random:
                if random in old_new_map:
                    new_node.random = old_new_map[random]
                else:
                    if random in waiting_nodes:
                        waiting_nodes[random].append(new_node)
                    else:
                        waiting_nodes[random] = [new_node]
            
            head = head.next
        
        return new_head