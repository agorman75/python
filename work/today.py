import os
import datetime

today = datetime.date.today
today = str(today)

location = r'D:\\test\\Reporting\\CFCPM_errors\\'
searchfile = open("D:\\test\\Reporting\\CFCPM_errors\\5951785.txt", "r")

import os
import datetime as dt

today = dt.datetime.now().date()

for file in os.listdir(location):
    filetime = dt.datetime.fromtimestamp(
            os.path.getctime(location + file))
    if filetime.date() == today:
        print(filetime)