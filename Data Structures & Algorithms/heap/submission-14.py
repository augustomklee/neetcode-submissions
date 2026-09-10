class MinHeap:
    
    def __init__(self):
        self.heap = [-1]
        # i = current
        # 2 * i = left child
        # 2 * i + 1 = right child
        # i // 2 = parent

    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1
        self.percolateUp(i)

    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()

        # replace min node with last value of heap
        minNode = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.percolateDown(1)
        return minNode

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = [-1] + nums
        cur = len(nums) // 2
        while cur > 0:
            self.percolateDown(cur)
            cur -= 1

    def percolateUp(self, i) -> None:
        # while i has a parent and i is smaller than its parent
        while i // 2 >= 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2
    
    def percolateDown(self, i) -> None:
        # While left child exists
        while 2 * i < len(self.heap):
            smallest = i
            left = 2 * i
            right = 2 * i + 1

            # check left child
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left

            # check right child
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            
            if smallest == i:
                break
            
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest