import os 
import sys
# 获取当前脚本文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将上级目录（项目根目录）添加到系统路径中
project_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_dir)

from group4.toolbox.minheap import MinHeap
import unittest
from group4.toolbox.minheap import MinHeap

# 测试二进制堆实现
class TestMinHeap(unittest.TestCase):
    def test_insert_extract(self):
        pq = MinHeap()
        pq.insert('task1', 5)
        pq.insert('task2', 1)
        pq.insert('task3', 3)
        self.assertEqual(pq.extract_max(), 'task1')
        self.assertEqual(pq.extract_max(), 'task3')
        self.assertEqual(pq.extract_max(), 'task2')
        self.assertEqual(pq.extract_max(), None)

    def test_search(self):
        pq = MinHeap()
        pq.insert('task1', 5)
        pq.insert('task2', 1)
        pq.insert('task3', 3)
        node = pq.search('task2')
        self.assertIsNotNone(node)

    def test_change_priority(self):
        pq = MinHeap()
        pq.insert('task1', 5)
        pq.insert('task2', 1)
        pq.insert('task3', 3)
        pq.change_priority('task3', 6)
        self.assertEqual(pq.extract_max(), 'task3')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
