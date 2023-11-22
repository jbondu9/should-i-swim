from answers.enums import Reason


def get_lower_bound(status: str) -> int:
    if status == Reason.FEW_PEOPLE.name:
        return 20
    if status == Reason.HALF_FULL.name:
        return 40
    if status == Reason.CROWED.name:
        return 60
    if status == Reason.TOTALLY_FULL.name:
        return 80
    return 0


def get_open(status: str) -> bool:
    return status != Reason.CLOSED.name


def get_upper_bound(status: str) -> int:
    if status == Reason.NEARLY_EMPTY.name:
        return 20
    if status == Reason.FEW_PEOPLE.name:
        return 40
    if status == Reason.HALF_FULL.name:
        return 60
    if status == Reason.CROWED.name:
        return 80
    return 100
