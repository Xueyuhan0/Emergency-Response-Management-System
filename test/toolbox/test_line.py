import os 
import sys
# 获取当前脚本文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将上级目录（项目根目录）添加到系统路径中
project_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_dir)

from group4.toolbox.line import LinkedListPriorityQueue
import unittest
from group4.toolbox.line import LinkedListPriorityQueue

# 测试链表实现
class TestLinkedListPriorityQueue(unittest.TestCase):  # 定义一个继承自unittest.TestCase的类，用于包含针对LinkedListPriorityQueue类的测试方法。
    def test_insert_extract(self):  # 在测试类中定义一个测试方法，用于测试`insert`和`extract_max`方法。
        pq = LinkedListPriorityQueue()  # 创建一个LinkedListPriorityQueue对象。
        pq.insert('task1', 1)  # 插入一个优先级为1的任务'task1'。
        pq.insert('task2', 5)  # 插入一个优先级为5的任务'task2'。 
        pq.insert('task3', 3)  # 插入一个优先级为3的任务'task3'。
        self.assertEqual(pq.extract_max(), 'task2')   # 调用`extract_max`方法提取优先级最高的任务，并断言其返回值为'task2'。
        self.assertEqual(pq.extract_max(), 'task3')  # 再次调用`extract_max`方法，并断言其返回值为'task3'。  
        self.assertEqual(pq.extract_max(), 'task1')   # 再次调用`extract_max`方法，并断言其返回值为'task1'。
        self.assertEqual(pq.extract_max(), None)    # 当队列为空时，调用`extract_max`方法并断言其返回值为None。


    def test_search(self):
        pq = LinkedListPriorityQueue()
        pq.insert('task1', 1)
        pq.insert('task2', 5)
        pq.insert('task3', 3)
        node = pq.search('task2')
        self.assertIsNotNone(node)
        self.assertEqual(node.priority, 5)

    def test_change_priority(self):
        pq = LinkedListPriorityQueue()
        pq.insert('task1', 1)
        pq.insert('task2', 5)
        pq.insert('task3', 3)
        pq.change_priority('task3', 6)
        self.assertEqual(pq.extract_max(), 'task3')

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

