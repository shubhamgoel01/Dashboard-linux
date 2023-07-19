import requests
from requests.auth import HTTPBasicAuth
from urllib.request import urlopen
import json

# request_url = 'http://nagios.beta-wspbx.com/nagios/cgi-bin/statusjson.cgi?query=service&hostname=beta-161&servicedescription=Freeswitch'
# request_url = 'http://nagios.beta-wspbx.com/nagios/cgi-bin/statusjson.cgi?query=service&hostname=10.30.48.178&servicedescription=Streams'
request_url = 'http://nagios.beta-wspbx.com/nagios/cgi-bin/statusjson.cgi?query=service&hostname=10.30.48.194&servicedescription=wsumserver'

username = 'nagiosadmin'
password = 'nagios@beta'
session = requests.Session()
request = session.get(request_url, auth=HTTPBasicAuth(username,password), verify=False)
# data_json = json.loads(response.read())

print(request.text)
# print(request)
data_json = json.loads(request.text)
print(type(data_json))   # <class 'dict'>
print("----------------------------")
print(data_json["data"])
print("----------------------------")
print(data_json['data']['service']['plugin_output'])

# ---------------function to check if small string is - there in big string
def check(string, sub_str):
    if (string.find(sub_str) != -1) or (string.find(sub_str1) != -1):
        print("Yes")
    else:
        print("No")
            

# string = "HTTP OK: HTTP/1.1 200 - 435 bytes in 0.001 second response time"
string = data_json['data']['service']['plugin_output']
sub_str ="HTTP OK"
check(string, sub_str)