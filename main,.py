import os
import sys
# 获取当前脚本文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将上级目录（项目根目录）添加到系统路径中
project_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_dir)


import time
import pandas as pd
from group4.toolbox.emergency import Emergency, EmergencyType
from group4.toolbox.line import LinkedListPriorityQueue
from group4.toolbox.tree import BSTPriorityQueue
from group4.toolbox.minheap import MinHeap

def initialize_structures(file_path):
    data = pd.read_csv(file_path)
    
    linked_list_pq = LinkedListPriorityQueue()
    bst_pq = BSTPriorityQueue()
    heap_pq = MinHeap()
    
    for index, row in data.iterrows():
        emergency = Emergency(row['emergency_id'], EmergencyType[row['type'].upper()], row['severity'], row['location'])
        linked_list_pq.insert(emergency, row['severity'])
        bst_pq.insert(emergency, row['severity'])
        heap_pq.insert(emergency, row['severity'])
    
    return linked_list_pq, bst_pq, heap_pq

file_path = r"emergency_dataset.csv"
# 初始化结构
linked_list_pq, bst_pq, heap_pq = initialize_structures(file_path)

# 打印初始化后的结构
print("Linked List Priority Queue:")
print(linked_list_pq)

print("\nBST Priority Queue:")
print(bst_pq)

print("\nHeap Priority Queue:")
print(heap_pq)

def initialize_structures(file_path):
    data = pd.read_csv(file_path)

    linked_list_pq = LinkedListPriorityQueue()
    bst_pq = BSTPriorityQueue()
    heap_pq = MinHeap()

    for index, row in data.iterrows():
        emergency = Emergency(row['emergency_id'], EmergencyType[row['type'].upper()], row['severity'], row['location'])
        linked_list_pq.insert(emergency, row['severity'])
        bst_pq.insert(emergency, row['severity'])
        heap_pq.insert(emergency, row['severity'])

    return linked_list_pq, bst_pq, heap_pq


def compare_pq_performance(file_path):
    linked_list_pq, bst_pq, heap_pq = initialize_structures(file_path)

    # Measure insertion time
    start_time = time.time()
    # Perform insertions into linked_list_pq, bst_pq, heap_pq

    linked_list_insert_time = time.time() - start_time

    start_time = time.time()
    bst_insert_time = time.time() - start_time

    start_time = time.time()
    heap_insert_time = time.time() - start_time

    # Measure removal time (assuming removal from the front for linked list and BST)
    start_time = time.time()
    # Perform removals from linked_list_pq, bst_pq, heap_pq

    linked_list_remove_time = time.time() - start_time

    start_time = time.time()
    bst_remove_time = time.time() - start_time

    start_time = time.time()
    heap_remove_time = time.time() - start_time

    # Print results
    print("Performance Comparison of Priority Queues:")
    print("Insertion Time:")
    print(f"Linked List Priority Queue: {linked_list_insert_time:.6f} seconds")
    print(f"BST Priority Queue: {bst_insert_time:.6f} seconds")
    print(f"Heap Priority Queue: {heap_insert_time:.6f} seconds")

    print("\nRemoval Time:")
    print(f"Linked List Priority Queue: {linked_list_remove_time:.6f} seconds")
    print(f"BST Priority Queue: {bst_remove_time:.6f} seconds")
    print(f"Heap Priority Queue: {heap_remove_time:.6f} seconds")


if __name__ == "__main__":
    file_path = r"emergency_dataset.csv"
    compare_pq_performance(file_path)

  