import subprocess
from datetime import date
import time
import datetime

crt_day = " /usr/bin/openssl x509 -enddate -noout -in /opt/Dashboard_All/project1/extra/clients.crt  | awk '{print $2}'"
crt_day_result = subprocess.check_output(crt_day, shell=True)
crt_day_1 = crt_day_result.decode('utf-8').rstrip()
crt_year = "/usr/bin/openssl x509 -enddate -noout -in /opt/Dashboard_All/project1/extra/clients.crt  | awk '{print $4}'"  # Replace with your desired command
crt_year_result = subprocess.check_output(crt_year, shell=True)
crt_year_1 = crt_year_result.decode('utf-8').rstrip()
month_dict = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8', 'Sep': '9', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
crt_month = "/usr/bin/openssl x509 -enddate -noout -in /opt/Dashboard_All/project1/extra/clients.crt  | awk -F '=' '{print $2}' | cut -d '2' -f1 "  # Replace with your desired command
crt_month_result = subprocess.check_output(crt_month, shell=True)
crt_month_tmp = crt_month_result.decode('utf-8').rstrip()
if crt_month_tmp in month_dict.keys():
    crt_month_1 = month_dict[crt_month_tmp]
else:
    print("issue in crt_month_tmp")

m1 = int(crt_month_1)
d1 = int(crt_day_1)
y1 = int(crt_year_1)
current_time = datetime.datetime.now()
crt_year_2 = current_time.year
crt_month_2 = current_time.month
crt_day_2 = current_time.day

date1 = date(y1, m1, d1)
date2 = date(crt_year_2, crt_month_2, crt_day_2)
c = (date1-date2).days
print(c)
