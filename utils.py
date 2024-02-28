from datetime import timedelta


def convert_days_to_timedelta(days):
    integer_days = int(days)
    fractional_day = days - int(days)
    delta = timedelta(days=integer_days, seconds=int(fractional_day * 24 * 60 * 60))
    return delta



