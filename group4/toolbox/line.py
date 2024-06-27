class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None
class LinkedListPriorityQueue:
    def __init__(self):
        self.head = None

    def insert(self, data, priority):
        new_node = Node(data, priority)
        if not self.head or self.head.priority < priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.priority >= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def extract_max(self):
        if self.head:
            max_node = self.head
            self.head = self.head.next
            return max_node.data
        return None

    def __repr__(self):
        result = []
        current = self.head
        while current:
            result.append((current.data, current.priority))
            current = current.next
        return str(result)