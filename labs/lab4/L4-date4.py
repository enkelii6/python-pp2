from datetime import datetime
def diff(d1, d2):
    date1 = datetime.strptime(d1, "%Y-%d-%m %H:%M:%S")
    date2 = datetime.strptime(d2, "%Y-%d-%m %H:%M:%S")

    res = date2 - date1

    ressec = res.total_seconds()
    return ressec

datestr1 = '2020-12-12 12:00:00'
datestr2 = '2020-12-12 11:00:00'
print(diff(datestr1, datestr2))