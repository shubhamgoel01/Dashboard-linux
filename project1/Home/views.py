from cgitb import html
from multiprocessing import context
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from Home.models import WebBeta1, WebBeta2, WebBeta3, WebBeta4, NewUpdateInfo, RRFImage, IPTable
from django.contrib import messages
import requests
from requests.auth import HTTPBasicAuth
from urllib.request import urlopen
import json
import re
from django.urls import reverse
import numpy as np
from bs4 import BeautifulSoup
import subprocess
from datetime import date
import requests
import json
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException
import time
import datetime

# Create your views here.


def index(request):
    # List of certificate files with their full paths
    cert_files = {
        "cfgtre.beta-wspbx.com.crt": "/opt/Dashboard-linux/project1/extra/cfgtre.beta-wspbx.com.crt",
        "fwdin.beta-wspbx.com.crt": "/opt/Dashboard-linux/project1/extra/fwdin.beta-wspbx.com.crt",
        "mp88.beta-wspbx.com.crt": "/opt/Dashboard-linux/project1/extra/mp88.beta-wspbx.com.crt",
        "p101.beta-wspbx.com.crt": "/opt/Dashboard-linux/project1/extra/p101.beta-wspbx.com.crt",
        "p103.beta-wspbx.com.crt": "/opt/Dashboard-linux/project1/extra/p103.beta-wspbx.com.crt",
        "p104.beta-wspbx.com.crt": "/opt/Dashboard-linux/project1/extra/p104.beta-wspbx.com.crt",
        "p107.beta-wspbx.com.crt": "/opt/Dashboard-linux/project1/extra/p107.beta-wspbx.com.crt",
        "p201.beta-wspbx.com.crt": "/opt/Dashboard-linux/project1/extra/p201.beta-wspbx.com.crt",
        "p801.beta-wspbx.com.crt": "/opt/Dashboard-linux/project1/extra/p801.beta-wspbx.com.crt",
        "SANp103.beta-wspbx.com.crt": "/opt/Dashboard-linux/project1/extra/SANp103.beta-wspbx.com.crt",
        "sms-wspbx-com.crt": "/opt/Dashboard-linux/project1/extra/sms-wspbx-com.crt",
        "wild.beta-wspbx.com.crt": "/opt/Dashboard-linux/project1/extra/wild.beta-wspbx.com.crt",
        "clients.crt": "/opt/Dashboard-linux/project1/extra/clients.crt"
    }

    # String to store certificate expiry information
    expiry_info = ""

    # Iterate through each certificate file
    for cert_name, cert_path in cert_files.items():
        # Run shell command to get the end date of the certificate
        end_date_command = f"/usr/bin/openssl x509 -enddate -noout -in {cert_path}"
        end_date_result = subprocess.check_output(end_date_command, shell=True)
        end_date_string = end_date_result.decode('utf-8').strip().split('=')[1]

        # Parse the end date string to a datetime object
        end_date = datetime.datetime.strptime(end_date_string, '%b %d %H:%M:%S %Y %Z')

        # Calculate the number of days left until expiration
        days_left = (end_date - datetime.datetime.now()).days

        # Format the certificate expiry information and append to the output string
        expiry_info += f"{cert_name}: {days_left} days left until expiration, expiry date: {end_date.strftime('%Y-%m-%d %H:%M:%S %Z')}\n"

    data = RRFImage.objects.all()
    context = {
             'expiry_info':expiry_info,
             'data' : data
    }
    return render(request,'index.html',context)


def output(request):
   msg1=request.GET.get('buildno')
   msg2=request.GET.get('ipaddress')
   print(msg1,msg2)
   context = {
       'msg1':msg1,
       'msg2':msg2
   }        
   return render(request, 'output.html',context)
# --------------------------------------New ---------------
def checkupdate(request):  
    result_httpd = update_httpd("https://httpd.apache.org/download.cgi")
    result_openssl = update_openssl("https://www.openssl.org/")
    result_php = update_php("https://www.php.net/")
    result_Hadoop = update_Hadoop("https://hadoop.apache.org/release.html")
    result_ZooKeeper = update_ZooKeeper("https://zookeeper.apache.org/releases.html")
    result_Spark = update_Spark("https://spark.apache.org/downloads.html")
    result_tomcat = update_tomcat("https://tomcat.apache.org/")
    result_java = update_java("https://www.oracle.com/in/java/technologies/java-se-glance.html")
    result_activemq = update_activemq("https://activemq.apache.org/components/classic/download/")
    
    objNewUpdateInfo = NewUpdateInfo.objects.all().values() 
    # print(objNewUpdateInfo)
    context = {
       'result_httpd':result_httpd, 
       'result_openssl':result_openssl,     
       'result_php':result_php,    
       'result_Hadoop':result_Hadoop,    
       'result_ZooKeeper':result_ZooKeeper,    
       'result_Spark':result_Spark,    
       'result_tomcat':result_tomcat,    
       'result_java':result_java,    
       'result_activemq':result_activemq,    
       'objNewUpdateInfo':objNewUpdateInfo,  
       
   }        
    return render(request,'checkupdate.html',context)

def addinNewUpdateInfo(request):
   return render(request, 'newrecordincheckupdate.html')

def addrecordinNewUpdateInfo(request):
    x = request.POST['name']
    y = request.POST['beta']
    z = request.POST['production']
    print("output--------->",x,y,z)    
    obj = NewUpdateInfo(name=x, beta=y,production=z)
    obj.save()
    return HttpResponseRedirect(reverse('checkupdate'))

def deleteinNewUpdateInfo(request, id):
    print("inside del function ",id)
    delNewUpdateInfo = NewUpdateInfo.objects.get(id=id)
    delNewUpdateInfo.delete()
    return HttpResponseRedirect(reverse('checkupdate'))

def updateinNewUpdateInfo(request, id):
  updateobj = NewUpdateInfo.objects.get(id=id) 
  template = loader.get_template('updatecheckupdate.html')
  context = {
    'updateobj': updateobj,
  }
  return HttpResponse(template.render(context, request))

def updaterecordNewUpdateInfo(request, id):
  name = request.POST['name']
  beta = request.POST['beta']
  production = request.POST['production']
  member = NewUpdateInfo.objects.get(id=id)
  member.name = name
  member.beta = beta
  member.production = production
  member.save()
  return HttpResponseRedirect(reverse('checkupdate'))

# ----------------------------------------------------end----

def IPTables(request):
    iptable_objs = IPTable.objects.filter(service_name="IPTables")
    base_url = "http://nagios.beta-wspbx.com/nagios/cgi-bin/statusjson.cgi?query=service"

    url_info_list_run = []  # Create an empty list to store URL and info
    url_info_list_nrun = []  # Create an empty list to store URL and info

    for iptable_obj in iptable_objs:
        service_name = iptable_obj.service_name
        ip1 = iptable_obj.ip1

        # Use the values from each object to construct the URL
        constructed_url = f"{base_url}&hostname={ip1}&servicedescription={service_name}"

        # Now, you have the constructed URL for each matching object
        # print(constructed_url)
        test = webnagios(constructed_url)

        if test == 'Running':            
            # Append the URL and info to the list
            url_info_list_run.append(ip1)
        else:
            url_info_list_nrun.append(ip1)
  
    context = {
        'url_info_list_run': url_info_list_run,  # Pass the list in the context
        'url_info_list_nrun': url_info_list_nrun,  # Pass the list in the context
    }
    return render(request, 'IPTables.html', context)

def services(request):
   build1=request.GET.get('buildno')
   build2=request.GET.get('ipaddress')
   print(build1,build2)
   return render(request, 'services.html',{'build1':build1,'build2':build2})

def pbx(request):
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    WebB1 = WebBeta2.objects.all().values()   
    # print("------------------Query set output  PBX--------------------")    
    # print(WebB1)    
    # Converted Queryset obj to list
    i = 0
    data = []
    for row in WebB1:
        while i < len(WebB1):
            tmp = list((WebB1[i]).values())
            i = i + 1
            data.append(tmp)
    # print("\n\n -----------Converted Queryset obj to list PBX OUTPUT -------------")
    # print(data)
    # Assigned service data(status,ip,servicename)  into 3 list accordingly
    counter1 = 0    #  number of object /service in WebB1
    service_status = []
    service_status_ip = []
    service_status_name = []
    for x in data:
        while counter1 < len(data):
            service_name = data[counter1][1]
            service_ip = data[counter1][2:]           
            counter1 = counter1 + 1
            # creating URL for API Hit in nagios
            if (service_ip[0] != '' ):
                serviceurl1 = UrlReturn(service_name, service_ip[0])                
                res1 = webnagios(serviceurl1)                
            else:
                res1 = 'Absent'
                
            if (service_ip[1] != '' ):
                serviceurl2 = UrlReturn(service_name, service_ip[1])    
                # print("--serviceurl2 printing---",serviceurl2)            
                res2 = webnagios(serviceurl2)                
            else:
                res2 = 'Absent'
            if (service_ip[2] != '' ):
                serviceurl3 = UrlReturn(service_name, service_ip[2])                
                res3 = webnagios(serviceurl3)                
            else:
                res3 = 'Absent'
            if (service_ip[3] != '' ):
                serviceurl4 = UrlReturn(service_name, service_ip[3])                
                res4 = webnagios(serviceurl4)                
            else:
                res4 = 'no'
            if (service_ip[4] != '' ):
                serviceurl5 = UrlReturn(service_name, service_ip[4])                
                res5 = webnagios(serviceurl5)                
            else:
                res5 = 'no'
                
            # serviceurl1 = UrlReturn(service_name, service_ip[0])
            # serviceurl2 = UrlReturn(service_name, service_ip[1])
            # serviceurl3 = UrlReturn(service_name, service_ip[2])
            # d = UrlReturn(service_name, service_ip[3])     
            # e = UrlReturn(service_name, service_ip[4])
            # NOTE: write function to check IP is pattern or not , if not , dont run function
            # res1 = webnagios(serviceurl1)
            # res2 = webnagios(serviceurl2)
            # res3 = webnagios(serviceurl3)
            # res4 = webnagios(d) 
            # res4 = webnagios(e)
            service_status.append(res1)
            service_status_ip.append(service_ip[0])
            service_status_name.append(service_name)
            service_status.append(res2)
            service_status_ip.append(service_ip[1])
            service_status_name.append(service_name)
            service_status.append(res3)
            service_status_ip.append(service_ip[2])
            service_status_name.append(service_name)
            service_status.append(res4)
            service_status_ip.append(service_ip[3])
            service_status_name.append(service_name)
            service_status.append(res5)
            service_status_ip.append(service_ip[4])
            service_status_name.append(service_name)
            # print("@@@@@@@@@@@@@@@@@@@",service_name,service_ip)            
            # print('^^^^^^^^^',service_status,service_status_ip,service_status_name)           
   
 
    op =  zip(service_status_name, service_status_ip, service_status)
    # print("-------------------------")
    # print(service_status)
    # print(service_status_ip)
    # print(service_status_name)
    print(op)
    cc = list(op)
    # print(cc)
    lengthofservice = len(WebB1)
    finalpass = np.reshape(cc,(lengthofservice,5,3))
    # print(finalpass)
 
    context = {       
        'data':data,   
        'service_status':service_status,   
        'service_status_ip':service_status_ip,
        'service_status_name':service_status_name,
        'WebB1':WebB1,  
        'aaaa' : op,  
        'finalpass' : finalpass,  
        
    }     
    return render(request, 'pbx.html',context)
 


def web(request):
    print("+++++++++++++++++WEB REQUEST+++++++++++++++++++++++++++++++++++++++++++++++++++++")
    WebB1 = WebBeta1.objects.all().values()   
    # print("------------------Query set output --------------------")    
    # print(WebB1)    
    # Converted Queryset obj to list
    i = 0
    data = []
    for row in WebB1:
        while i < len(WebB1):
            tmp = list((WebB1[i]).values())
            i = i + 1
            data.append(tmp)
    # print("\n\n ------------Converted Queryset obj to list WEB OUTPUT -------------")
    # print(data)
    # Assigned service data(status,ip,servicename)  into 3 list accordingly
    counter1 = 0    #  number of object /service in WebB1
    service_status = []
    service_status_ip = []
    service_status_name = []
    for x in data:
        while counter1 < len(data):
            service_name = data[counter1][1]
            service_ip = data[counter1][2:]           
            counter1 = counter1 + 1
            # creating URL for API Hit in nagios
            if (service_ip[0] != '' ):
                serviceurl1 = UrlReturn(service_name, service_ip[0])                
                res1 = webnagios(serviceurl1)                
            else:
                res1 = 'Absent'
                
            if (service_ip[1] != '' ):
                serviceurl2 = UrlReturn(service_name, service_ip[1])    
                # print("--serviceurl2 printing---",serviceurl2)            
                res2 = webnagios(serviceurl2)                
            else:
                res2 = 'Absent'
            if (service_ip[2] != '' ):
                serviceurl3 = UrlReturn(service_name, service_ip[2])                
                res3 = webnagios(serviceurl3)                
            else:
                res3 = 'Absent'
            if (service_ip[3] != '' ):
                serviceurl4 = UrlReturn(service_name, service_ip[3])                
                res4 = webnagios(serviceurl4)                
            else:
                res4 = 'no'
            if (service_ip[4] != '' ):
                serviceurl5 = UrlReturn(service_name, service_ip[4])                
                res5 = webnagios(serviceurl5)                
            else:
                res5 = 'no'
                
            # serviceurl1 = UrlReturn(service_name, service_ip[0])
            # serviceurl2 = UrlReturn(service_name, service_ip[1])
            # serviceurl3 = UrlReturn(service_name, service_ip[2])
            # d = UrlReturn(service_name, service_ip[3])     
            # e = UrlReturn(service_name, service_ip[4])
            # NOTE: write function to check IP is pattern or not , if not , dont run function
            # res1 = webnagios(serviceurl1)
            # res2 = webnagios(serviceurl2)
            # res3 = webnagios(serviceurl3)
            # res4 = webnagios(d) 
            # res4 = webnagios(e)
            service_status.append(res1)
            service_status_ip.append(service_ip[0])
            service_status_name.append(service_name)
            service_status.append(res2)
            service_status_ip.append(service_ip[1])
            service_status_name.append(service_name)
            service_status.append(res3)
            service_status_ip.append(service_ip[2])
            service_status_name.append(service_name)
            service_status.append(res4)
            service_status_ip.append(service_ip[3])
            service_status_name.append(service_name)
            service_status.append(res5)
            service_status_ip.append(service_ip[4])
            service_status_name.append(service_name)
            # print("@@@@@@@@@@@@@@@@@@@",service_name,service_ip)            
            # print('^^^^^^^^^',service_status,service_status_ip,service_status_name)           
   
 
    op =  zip(service_status_name, service_status_ip, service_status)
    # print("-------------------------")
    # print(service_status)
    # print(service_status_ip)
    # print(service_status_name)
    print(op)
    cc = list(op)
    # print(cc)
    lengthofservice = len(WebB1)
    finalpass = np.reshape(cc,(lengthofservice,5,3))
    # print(finalpass)
 
    context = {       
        'data':data,   
        'service_status':service_status,   
        'service_status_ip':service_status_ip,
        'service_status_name':service_status_name,
        'WebB1':WebB1,  
        'aaaa' : op,  
        'finalpass' : finalpass,  
        
    }     
    return render(request, 'web.html',context)
    # return render(request, 'web.html',{'result_streams178':result_streams178,'result_streams183':result_streams183,'result_streams185':result_streams185})

# ------------------------- shubham --------------------------------------------------------------------------------------------------------------------
def webnagios(passing_url):
    try:
        request_url = passing_url
        username = 'nagiosadmin'
        password = 'Nagios@beta'
        session = requests.Session()
        request = session.get(request_url, auth=HTTPBasicAuth(username, password), verify=False)
        request.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        data_json = json.loads(request.text)
        plugin_output = data_json['data']['service']['plugin_output']

        sub_str = "OK"
        sub_str1 = "ok"

        if (plugin_output.lower().find(sub_str.lower()) != -1) or (plugin_output.lower().find(sub_str1.lower()) != -1):
            return "Running"
        else:
            return "Not Running"

    except RequestException as e:
        # Handle the request exception (e.g., incorrect URL, network issues)
        return f"Error: {e}"

    except (KeyError, json.JSONDecodeError) as e:
        # Handle KeyError (missing keys in the JSON response) or JSON decoding errors
        return f"Error parsing JSON response: {e}"      
 
                
def UrlReturn(service_name,instance_ip):
    return("http://nagios.beta-wspbx.com/nagios/cgi-bin/statusjson.cgi?query=service&hostname=" + instance_ip + "&servicedescription=" + service_name)
      
# ---------------Apache oepnSSL---------------   
def update_httpd(passing_url):  
    resp=requests.get(passing_url)
    if resp.status_code==200:     
        soup=BeautifulSoup(resp.text,'html.parser')        
        l=soup.find("h1",{"id":"apache24"})
        # print(l.text)
        return(l.text)         
    else:      
        return(resp.status_code)
        # print('Error: %s' % resp.status_code)  
        
# ---------------OpenSSL---------------       
def update_openssl(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Define the version string pattern
        version_pattern = re.compile(r'OpenSSL\s+3\.0\.\d+')

        # Find all occurrences of the version string pattern in the page
        occurrences = soup.body(text=version_pattern.search)

        # If there are occurrences, return the first one
        if occurrences:
            latest_version = occurrences[0].strip()
            return latest_version
        else:
            return "No version strings matching 'OpenSSL 3.0.x' found on the OpenSSL website."
    else:
        return f"Failed to retrieve the webpage. Status code: {response.status_code}"
          
  
def update_php(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Define the version string pattern
        version_pattern = re.compile(r'PHP 8\.2\.\d+')

        # Find all occurrences of the version string pattern in the page
        occurrences = soup.body(text=version_pattern.search)

        # If there are occurrences, return the first one
        if occurrences:
            latest_version = occurrences[0].strip()
            return latest_version
        else:
            return "No version strings matching 'PHP 8.2.x' found on the PHP official website."
    else:
        return f"Failed to retrieve the webpage. Status code: {response.status_code}" 
    
    
# ---------------Hadoop---------------
def update_Hadoop(passing_url):  
    resp=requests.get(passing_url)
    if resp.status_code==200:      
        soup=BeautifulSoup(resp.text,'html.parser')        
        l=soup.find("ul",{"id":"list"})
        m = l.find("h1")
        return(m.text)          
    else:
        return(resp.status_code) 
    

def update_ZooKeeper(passing_url):     
    resp=requests.get(passing_url)
    if resp.status_code==200:      
        soup=BeautifulSoup(resp.text,'html.parser')        
        l=soup.find("div",{"class":"container"})       
        m = l.find_all("p")[4]
        return(m.text)                 
    else:
        return(resp.status_code) 

# -------------Tomcat --------------
def update_tomcat(passing_url):    
    resp=requests.get(passing_url)
    if resp.status_code==200:      
        soup=BeautifulSoup(resp.text,'html.parser')        
        l=soup.find("div",{"id":"content"})        
        m = l.find_all("h3")[1]
        return(m.text)                 
    else:
        return(resp.status_code) 

# -------------JAVA -------------
def update_java(passing_url): 
    resp=requests.get(passing_url)
    if resp.status_code==200:      
        soup=BeautifulSoup(resp.text,'html.parser')        
        l=soup.find("ul",{"class":"cta-list"})    
        m = l.find_all("li")[0]
        n = m.find("p")        
        return(n.text)        
    else:
        return(resp.status_code) 
    
# -------------Apache Spark -------------
def update_Spark(passing_url):  
    resp=requests.get(passing_url)
    if resp.status_code==200:      
        soup=BeautifulSoup(resp.text,'html.parser')        
        l=soup.find("pre",{"class":"highlight"}) 
        return(l.text)        
    else:
        return(resp.status_code) 
    
# ------------update record beta prod CRUD -------------
def update_activemq(passing_url):  
    resp=requests.get(passing_url)
    if resp.status_code==200:      
        soup=BeautifulSoup(resp.text,'html.parser')        
        l=soup.find("h4") 
        return(l.text)        
    else:
        return(resp.status_code) 

