
from datetime import datetime, timezone
from calendar import timegm
from typing import Optional

from django.conf import settings








def aware_utcnow() -> datetime:
    '''текущее время'''
    dt = datetime.now(tz=timezone.utc)
    if not settings.USE_TZ:
        dt = dt.replace(tzinfo=None)
    return dt


def datetime_from_epoch(ts: float) -> datetime:
    '''выдает дату в datetime формате'''
    dt = datetime.fromtimestamp(ts, tz=timezone.utc)
    if not settings.USE_TZ:
        dt = dt.replace(tzinfo=None)

    return dt


def datetime_to_epoch(dt: datetime) -> int:
    return timegm(dt.utctimetuple())



def old_life(iat_value, claim_value):
    '''проверка на процентность жизни refresh токена'''
    current_time = aware_utcnow()

    iat_value = datetime_from_epoch(iat_value)
    claim_value = datetime_from_epoch(claim_value)
    full_lifetime = claim_value - iat_value

    # Оставшееся время жизни
    remaining_lifetime = claim_value - current_time

    if remaining_lifetime > 0.4 * full_lifetime:
        return True #вернуть только access
    else:
        return False
