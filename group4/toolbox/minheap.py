class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, data, priority):
        self.heap.append((priority, data))
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) > 1:
            self._swap(0, len(self.heap) - 1)
            min_value = self.heap.pop()
            self._heapify_down(0)
        elif self.heap:
            min_value = self.heap.pop()
        else:
            min_value = None
        return min_value[1] if min_value else None

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index][0] < self.heap[parent_index][0]:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        child_index = 2 * index + 1
        if child_index < len(self.heap):
            right_child_index = child_index + 1
            if right_child_index < len(self.heap) and self.heap[right_child_index][0] < self.heap[child_index][0]:
                child_index = right_child_index
            if self.heap[child_index][0] < self.heap[index][0]:
                self._swap(child_index, index)
                self._heapify_down(child_index)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __repr__(self):
        return str([(data, priority) for priority, data in self.heap])

