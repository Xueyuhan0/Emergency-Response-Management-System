import os 
import sys
# 获取当前脚本文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将上级目录（项目根目录）添加到系统路径中
project_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_dir)


from group4.toolbox.emergency import Emergency
import unittest
from group4.toolbox.emergency import EmergencyType

class TestEmergency(unittest.TestCase):
    def test_emergency_creation(self):
        e = Emergency(1, EmergencyType.FIRE, 5, "Location A")
        '''assertEquals 如果预期值与真实值相等,则运行success,反之Failure'''
        self.assertEqual(e.emergency_id, 1)
        self.assertEqual(e.emergency_type, EmergencyType.FIRE)
        self.assertEqual(e.severity, 5)
        self.assertEqual(e.location, "Location A")
    
    def test_invalid_emergency_type(self):
        with self.assertRaises(ValueError):
            Emergency(2, "InvalidType", 3, "Location B")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)