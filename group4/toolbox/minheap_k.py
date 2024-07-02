
from group4.toolbox.emergency_k import calculate_distance
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, data, priority):
        self.heap.append((priority, data))
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()[1]
        self._swap(0, len(self.heap) - 1)
        min_value = self.heap.pop()
        self._heapify_down(0)
        return min_value[1]

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index][0] < self.heap[parent_index][0]:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left

        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right

        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __repr__(self):
        return str([(data, priority) for priority, data in self.heap])

def recommend_nearest_units(emergency, response_units, k):
    heap = MinHeap()
    for unit in response_units:
        distance = calculate_distance(emergency.x, emergency.y, unit.x, unit.y)
        heap.insert(unit, distance)

    nearest_units = []
    for _ in range(k):
        unit = heap.extract_min()
        if unit:
            nearest_units.append(unit)
    
    return nearest_units

