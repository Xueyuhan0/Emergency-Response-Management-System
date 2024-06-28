import os 
import sys
# 获取当前脚本文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将上级目录（项目根目录）添加到系统路径中
project_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_dir)

import unittest
from group4.toolbox.emergency import Emergency
from group4.toolbox.emergency import EmergencyType
from group4.toolbox.line import LinkedListPriorityQueue
from group4.toolbox.tree import BSTPriorityQueue
from group4.toolbox.minheap import MinHeap

import pandas as pd

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
