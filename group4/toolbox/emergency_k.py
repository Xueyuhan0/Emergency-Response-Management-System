# 扩展 Emergency 类
import math
from enum import Enum
import unittest

class EmergencyType(Enum):
    FIRE = 1
    MEDICAL = 2
    POLICE = 3

# 扩展 Emergency 类
class Emergency:
    def __init__(self, emergency_id, emergency_type, severity, location, x, y):
        self.emergency_id = emergency_id
        if isinstance(emergency_type, EmergencyType):
            self.emergency_type = emergency_type
        else:
            raise ValueError("Invalid emergency type")
        self.severity = severity
        self.location = location
        self.x = x
        self.y = y

    def __repr__(self):
        return (f"Emergency(ID: {self.emergency_id}, Type: {self.emergency_type}, "
                f"Severity: {self.severity}, Location: {self.location}, Coordinates: ({self.x}, {self.y}))")

    def __eq__(self, other):
        return (self.emergency_id == other.emergency_id and
                self.emergency_type == other.emergency_type and
                self.severity == other.severity and
                self.location == other.location and
                self.x == other.x and
                self.y == other.y)

# 创建 EmergencyResponseUnit 类
class EmergencyResponseUnit:
    def __init__(self, unit_id, unit_type, x, y):
        self.unit_id = unit_id
        self.unit_type = unit_type
        self.x = x
        self.y = y

    def __repr__(self):
        return f"EmergencyResponseUnit(ID: {self.unit_id}, Type: {self.unit_type}, Coordinates: ({self.x}, {self.y}))"

# 距离计算函数
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 初始化应急响应单元
response_units = [
    EmergencyResponseUnit(1, 'Fire Truck', 2, 3),
    EmergencyResponseUnit(2, 'Ambulance', 5, 4),
    EmergencyResponseUnit(3, 'Police Car', 1, 1)
]