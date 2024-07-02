# 打印推荐结果
from group4.toolbox.emergency_k import Emergency, EmergencyType
from group4.toolbox.minheap_k import recommend_nearest_units
from group4.toolbox.emergency_k import response_units

emergency = Emergency(1, EmergencyType.FIRE, 5, "Downtown", 0, 0)
k = 2
nearest_units = recommend_nearest_units(emergency, response_units, k)
print(f"The {k} nearest emergency response units are:")
for unit in nearest_units:
    print(unit)
