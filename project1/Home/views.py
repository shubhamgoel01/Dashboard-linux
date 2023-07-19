from cgitb import html
from multiprocessing import context
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from Home.models import WebBeta1, WebBeta2, WebBeta3,WebBeta4,NewUpdateInfo, RRFImage
from django.contrib import messages
import requests
from requests.auth import HTTPBasicAuth
from urllib.request import urlopen
import json
from django.urls import reverse
import numpy as np
from bs4 import BeautifulSoup
import subprocess
from datetime import date
import time
import datetime

# Create your views here.


def index(request):
    crt_day = " /usr/bin/openssl x509 -enddate -noout -in /opt/Dashboard-linux/project1/extra/clients.crt  | awk '{print $2}'"
    crt_day_result = subprocess.check_output(crt_day, shell=True)
    crt_day_1 = crt_day_result.decode('utf-8').rstrip()
    crt_year = "/usr/bin/openssl x509 -enddate -noout -in /opt/Dashboard-linux/project1/extra/clients.crt  | awk '{print $4}'"  # Replace with your desired command
    crt_year_result = subprocess.check_output(crt_year, shell=True)
    crt_year_1 = crt_year_result.decode('utf-8').rstrip()
    month_dict = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8', 'Sep': '9', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    crt_month = "/usr/bin/openssl x509 -enddate -noout -in /opt/Dashboard-linux/project1/extra/clients.crt  | awk -F '=' '{print $2}' | cut -d '2' -f1 "  # Replace with your desired command
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
    print("days_left",c)

    data = RRFImage.objects.all()
    context = {
             'day_left':c,
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
    result_openssl = update_openssl("https://www.openssl.org/source/")
    result_php = update_php("https://www.php.net/downloads.php")
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

def about(request):
    # Streamsbeta1obj =  list(WebBeta1.objects.values_list('service_name','ip1','ip2','ip3','ip4'))
    # Streamsbeta1obj =  WebBeta1.objects.filter(service_name='Streams').values()
    Streamsbeta1 =  list(WebBeta1.objects.filter(service_name='Streams').values())
    Streamsbeta2 =  list(WebBeta2.objects.filter(service_name='Streams').values())
    Admin5beta1 =  list(WebBeta1.objects.filter(service_name='Admin5').values())
    print("$$$$$$$$$$$",Streamsbeta1)  
    for i in  Streamsbeta1:
        print(i['service_name'])
    print("-------------------------------------------") 
    # print(type(Streamsbeta1)) // list  
    print(Streamsbeta1[0])      
 
    context = {
        'Streamsbeta1':Streamsbeta1,
        'Streamsbeta2':Streamsbeta2,  
        'Admin5beta1':Admin5beta1,        
    }
    return render(request,'about.html',context)

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
    request_url = passing_url
    # print("\n\n -----------  webnagios  function    --------------------    ")
    print(passing_url)
    # request_url = 'http://nagios.beta-wspbx.com/nagios/cgi-bin/statusjson.cgi?query=service&hostname=10.30.48.183&servicedescription=Streams'
    username = 'nagiosadmin'
    password = 'Nagios@beta'
    session = requests.Session()
    request = session.get(request_url, auth=HTTPBasicAuth(username,password), verify=False) 
    data_json = json.loads(request.text)   
    # print("----------------------------")
    # print(data_json['data']['service']['plugin_output'])
    
    string = data_json['data']['service']['plugin_output']
    # print("search string is " + string)
    sub_str ="OK" 
    sub_str1 ="ok" 
   
    if (string.find(sub_str) != -1) or (string.find(sub_str1) != -1):
        # print("function-webnagios :Yes")
        flag = "Running"
        print("function-webnagios : yes",passing_url)
        # print("----Running test here ----",string)
        return flag
    else:      
        print(" \n service not running ---------",passing_url , string)       
        flag = "Not Running" 
        return flag      
 
                
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
def update_openssl(passing_url):   
    resp=requests.get(passing_url)
    if resp.status_code==200:
        soup=BeautifulSoup(resp.text,'html.parser')        
        l=soup.find("article")
        m = l.findAll("table")[1]
        n = m.findAll("td")[8] 
        return(n.text)           
    else:
        return(resp.status_code) 
          
  
def update_php(passing_url):  
    resp=requests.get(passing_url)
    if resp.status_code==200:      
        soup=BeautifulSoup(resp.text,'html.parser')        
        l=soup.find("section",{"id":"layout-content"})
        m = l.findAll("h3")[0]
        return(m.text)           
    else:
        return(resp.status_code) 
    
    
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

