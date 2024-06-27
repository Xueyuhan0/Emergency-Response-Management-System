class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, data, priority):
        self.heap.append((priority, data))
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()[1]
        self._swap(0, len(self.heap) - 1)
        max_value = self.heap.pop()
        self._heapify_down(0)
        return max_value[1]

    def search(self, data):
        for priority, item in self.heap:
            if item == data:
                return item
        return None

    def change_priority(self, data, new_priority):
        for i, (priority, item) in enumerate(self.heap):
            if item == data:
                self.heap.pop(i)
                self._heapify_down(i)
                self.insert(data, new_priority)
                break

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index][0] > self.heap[parent_index][0]:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left][0] > self.heap[largest][0]:
            largest = left

        if right < len(self.heap) and self.heap[right][0] > self.heap[largest][0]:
            largest = right

        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __repr__(self):
        return str([(data, priority) for priority, data in self.heap])

