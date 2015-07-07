from dateutil import parser
import datetime
import time

def timestamp_in_date_range(stamp, start_date, end_date):
    """ return True if stamp between start_date and end_date, else False
        Parameters should following the formats below
        Examples:
            stamp  1435132892
            start_date  2015-06-01 00:00:00
            end_date  2015-06-02 00:00:00
            return False
    """
    start_date = parser.parse(start_date)
    end_date = parser.parse(end_date)
    examine_date = datetime.datetime.fromtimestamp(stamp)

    return start_date <= examine_date <= end_date
