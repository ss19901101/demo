from enum import Enum


class IntEnum(int, Enum):
    """Enum for numbers """


class DeviceStatus(IntEnum):
    ACTIVE = 1
    INACTIVE = 0
    UNKNOWN = 3
