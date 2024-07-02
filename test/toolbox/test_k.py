# 单元测试
import os 
import sys
# 获取当前脚本文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 将上级目录（项目根目录）添加到系统路径中
project_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_dir)
from group4.toolbox.emergency_k import Emergency
import unittest
from group4.toolbox.emergency_k import EmergencyType
from group4.toolbox.emergency_k import EmergencyResponseUnit
from group4.toolbox.minheap_k import recommend_nearest_units
class TestEmergencyResponse(unittest.TestCase):
    def test_recommend_nearest_units(self):
        emergency = Emergency(1, EmergencyType.FIRE, 5, "Downtown", 0, 0)
        response_units = [
            EmergencyResponseUnit(1, 'Fire Truck', 2, 3),
            EmergencyResponseUnit(2, 'Ambulance', 5, 4),
            EmergencyResponseUnit(3, 'Police Car', 1, 1)
        ]
        k = 2
        nearest_units = recommend_nearest_units(emergency, response_units, k)
        self.assertEqual(len(nearest_units), 2)
        self.assertEqual(nearest_units[0].unit_id, 3)
        self.assertEqual(nearest_units[1].unit_id, 1)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
