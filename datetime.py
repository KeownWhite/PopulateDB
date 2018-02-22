import calendar
from datetime import date, timedelta
import random

def rand_dates(max_days=1, year=None):

    while True:
        y = year or date.today().year
        m = random.randint(1, 12)
        d = random.randint(1, calendar.monthrange(y, m)[1])
        days = random.randint(1, max_days) if max_days > 0 else 0
        start_date = date(y, m, d)
        yield start_date, start_date + timedelta(days=days)
