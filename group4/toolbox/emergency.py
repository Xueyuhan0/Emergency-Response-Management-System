from enum import Enum

class EmergencyType(Enum):
    FIRE = 1
    MEDICAL = 2
    POLICE = 3

class Emergency:
    def __init__(self, emergency_id, emergency_type, severity, location):
        self.emergency_id = emergency_id
        if isinstance(emergency_type, EmergencyType):
            self.emergency_type = emergency_type
        else:
            raise ValueError("Invalid emergency type")
        self.severity = severity
        self.location = location

    def __repr__(self):
        return (f"Emergency(ID: {self.emergency_id}, Type: {self.emergency_type}, "
                f"Severity: {self.severity}, Location: {self.location})")

    def __eq__(self, other):
        return (self.emergency_id == other.emergency_id and
                self.emergency_type == other.emergency_type and
                self.severity == other.severity and
                self.location == other.location)