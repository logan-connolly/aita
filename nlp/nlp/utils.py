import datetime


def get_date_stamp() -> str:
    """Get a date stamp YYYYMMDD to prepend to filenames"""
    dt = datetime.date.today()
    return dt.strftime("%Y%m%d")
