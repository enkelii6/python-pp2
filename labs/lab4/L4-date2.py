from datetime import datetime, timedelta
datestr = input("YYYY-MM-DD")
date = datetime.strptime(datestr, "%Y-%m-%d")
frmtd = date.strftime("%Y-%m-%d")
t = date + timedelta(days=1)
frm_t = t.strftime("%Y-%m-%d")
y = date - timedelta(days=1)
frm_y = y.strftime("%Y-%m-%d")
print(f"Today is {frmtd}, tommorow will be {frm_t} and yesterday was {frm_y}")