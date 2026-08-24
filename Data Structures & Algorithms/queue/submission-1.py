class ListNode:
    def __init__(self, val:int, next_node=None, prev_node=None):
        self.val = val
        self.next = next_node
        self.prev = prev_node
        
class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        prev = self.tail.prev 
    
        new_node.prev = prev 
        prev.next = new_node
        new_node.next = self.tail
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)
        next_node = self.head.next
        new_node.next = next_node
        next_node.prev = new_node
        new_node.prev = self.head
        self.head.next = new_node


    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last_node = self.tail.prev
        val = last_node.val
        prev_node = last_node.prev
        prev_node.next = self.tail
        self.tail.prev = prev_node
        return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        node = self.head.next
        val = node.val
        next_node = node.next
        self.head.next = next_node
        next_node.prev = self.head
        return val