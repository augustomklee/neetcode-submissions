class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    
    def __init__(self):
        self.left = LinkedNode(-1)
        self.right = LinkedNode(-1)
        self.left.next = self.right
        self.right.prev = self.left

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def append(self, value: int) -> None:
        new_node = LinkedNode(value)
        new_node.next = self.right  
        new_node.prev = self.right.prev
        self.right.prev = new_node
        new_node.prev.next = new_node

    def appendleft(self, value: int) -> None:
        new_node = LinkedNode(value)
        new_node.prev = self.left  
        new_node.next = self.left.next
        self.left.next = new_node
        new_node.next.prev = new_node

    def pop(self) -> int:
        if self.right.prev == self.left:
            return -1
        res = self.right.prev.val
        self.right.prev = self.right.prev.prev
        self.right.prev.next = self.right
        return res

    def popleft(self) -> int:
        if self.left.next == self.right:
            return -1
        res = self.left.next.val
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        return res
