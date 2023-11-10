from datetime import datetime, timedelta, timezone


def time_difference_from_now(time: datetime, tz: timezone = timezone.utc) -> timedelta:
    return datetime.now(tz) - time.replace(tzinfo=tz)
