import requests


def news():
	# the target we want to open	
	# url='http://nagios.beta-wspbx.com/nagios/cgi-bin/extinfo.cgi?type=2&host=beta-161&service=Freeswitch'
	url='http://192.168.1.8/wsvn/'
	# url='http://nagios.beta-wspbx.com/nagios/cgi-bin/statusjson.cgi?query=service&hostname=10.30.48.183&servicedescription=Streams'
	
	#open with GET method
	resp=requests.get(url)
	
	#http_respone 200 means OK status
	if resp.status_code==200:
		print("Successfully opened the web page")
		print("------------ :-\n")

	else:
		print("Error")
		
news()
