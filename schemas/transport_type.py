from enum import Enum

class TransportType(str, Enum):
    PLANE = "Plane"
    BUS = "Bus"
    INDIVIDUAL = "Individual"