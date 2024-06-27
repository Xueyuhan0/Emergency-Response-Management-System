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

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def change_priority(self, data, new_priority):
        if not self.head:
            return
        if self.head.data == data:
            self.head.priority = new_priority
        else:
            current = self.head
            while current.next and current.next.data != data:
                current = current.next
            if current.next:
                node_to_change = current.next
                current.next = node_to_change.next
                self.insert(data, new_priority)


    def __repr__(self):
        result = []
        current = self.head
        while current:
            result.append((current.data, current.priority))
            current = current.next
        return str(result)

