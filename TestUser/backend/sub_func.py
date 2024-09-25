
from datetime import datetime, timezone
from calendar import timegm


from django.conf import settings











def aware_utcnow() -> datetime:
    dt = datetime.now(tz=timezone.utc)
    if not settings.USE_TZ:
        dt = dt.replace(tzinfo=None)
    return dt


def datetime_from_epoch(ts: float) -> datetime:
    dt = datetime.fromtimestamp(ts, tz=timezone.utc)
    if not settings.USE_TZ:
        dt = dt.replace(tzinfo=None)

    return dt


def datetime_to_epoch(dt: datetime) -> int:
    return timegm(dt.utctimetuple())
