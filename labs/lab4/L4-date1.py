from datetime import datetime, timedelta
datestr = input("YYYY-MM-DD")
date = datetime.strptime(datestr, "%Y-%m-%d")
res = date - timedelta(days=5)
frmres = res.strftime("%Y-%m-%d")
print(frmres)
