import subprocess
from datetime import date
import time
import datetime




hostname = " hostname "
hostname_result = subprocess.check_output(hostname, shell=True)
hostname_tmp = hostname_result.decode('utf-8').rstrip()
print("###################################################\nHostname: \n",hostname_tmp)

model = " lshw -c system | grep product "
model_result = subprocess.check_output(model, shell=True)
model_tmp = model_result.decode('utf-8').rstrip()
print("###################################################\n Physical and model number was : \n",model_tmp)

local_ip = " hostname -I "
local_ip_result = subprocess.check_output(local_ip, shell=True)
local_ip_tmp = local_ip_result.decode('utf-8').rstrip()
print("###################################################\nlocal_ip: \n",local_ip_tmp)
