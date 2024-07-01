import os 
import sys
# 获取当前脚本文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将上级目录（项目根目录）添加到系统路径中
project_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_dir)

from group4.toolbox.tree import BSTPriorityQueue
import unittest
from group4.toolbox.tree import BSTPriorityQueue
# 测试二叉搜索树实现
class TestBSTPriorityQueue(unittest.TestCase):  # 定义一个名为TestBSTPriorityQueue的类，它继承自unittest.TestCase。  
# 这个类将包含对BSTPriorityQueue类的测试方法。  
    def test_insert_extract(self):  # 在TestBSTPriorityQueue类中定义一个测试方法test_insert_extract。  
    # 这个方法将测试BSTPriorityQueue的insert和extract_max方法。  
        pq = BSTPriorityQueue()  # 创建一个BSTPriorityQueue对象pq。
        pq.insert('task1', 1)   # 调用pq的insert方法，插入一个优先级为1的任务'task1'。
        pq.insert('task2', 5)  # 插入一个优先级为5的任务'task2'。 
        pq.insert('task3', 3)   # 插入一个优先级为3的任务'task3'。
        self.assertEqual(pq.extract_max(), 'task2')   # 调用pq的extract_max方法并断言其返回值（即提取的具有最高优先级的任务）为'task2'。
        self.assertEqual(pq.extract_max(), 'task3')   # 再次调用extract_max并断言其返回值为'task3'。  
        self.assertEqual(pq.extract_max(), 'task1')    # 再次调用extract_max并断言其返回值为'task1'。
        self.assertEqual(pq.extract_max(), None)    # 调用extract_max并断言其返回值为None，因为此时队列已经为空。 

    def test_search(self):
        pq = BSTPriorityQueue()
        pq.insert('task1', 1)
        pq.insert('task2', 5)
        pq.insert('task3', 3)
        node = pq.search('task2')
        self.assertIsNotNone(node)
        self.assertEqual(node.priority, 5)

    def test_change_priority(self):
        pq = BSTPriorityQueue()
        pq.insert('task1', 1)
        pq.insert('task2', 5)
        pq.insert('task3', 3)
        pq.change_priority('task3', 6)
        self.assertEqual(pq.extract_max(), 'task3')

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)