import os 
import sys
# 获取当前脚本文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将上级目录（项目根目录）添加到系统路径中
project_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_dir)

from group4.toolbox.line import LinkedListPriorityQueue # type: ignore
import unittest
from group4.toolbox.line import LinkedListPriorityQueue # type: ignore

#测试链表实现
class TestLinkedListPriorityQueue(unittest.TestCase):
    def test_insert_extract(self):
        pq = LinkedListPriorityQueue() 
        pq.insert('task1', 1)
        pq.insert('task2', 5)
        pq.insert('task3', 3)
        self.assertEqual(pq.extract_max(), 'task2')
        self.assertEqual(pq.extract_max(), 'task3')
        self.assertEqual(pq.extract_max(), 'task1')
        self.assertEqual(pq.extract_max(), None)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
