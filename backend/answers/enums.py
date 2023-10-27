from enum import Enum


class Reason(Enum):
    CLOSED = "CLOSED"
    NEARLY_EMPTY = "NEARLY_EMPTY"
    FEW_PEOPLE = "FEW_PEOPLE"
    HALF_FULL = "HALF_FULL"
    CROWED = "CROWED"
    TOTALLY_FULL = "TOTALLY_FULL"
