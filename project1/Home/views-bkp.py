from cgitb import html
from multiprocessing import context
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from Home.models import Contact
from django.contrib import messages
import requests
from requests.auth import HTTPBasicAuth
from urllib.request import urlopen
import json
from django.urls import reverse

# Create your views here.
def index(request):
    mycontact = Contact.objects.all().values()    
    print(mycontact)
    # print(type(mycontact))   // django.db.models.query.QuerySet
    tname = "" 
    tmail = "" 
    for x in mycontact:
        tname += x["name"]
        tmail += x["email"]
    
    # print(type(tmail))   // str
    context = {
        'build':"build-Number",
        'ip':"IP",
        'out1':tname,
        'out2':tmail,
        'mycontact':mycontact,
    }  
    # return HttpResponse(output)
    return render(request,'index.html',context)

def add(request):
    # template = loader.get_template('add.html')
    # return HttpResponse(template.render({}, request))
   return render(request, 'add.html')

def addrecord(request):
    x = request.POST['name']
    y = request.POST['email']
    print("yssssss",x,y)
    print(type(x))
    contact = Contact(name=x, email=y)
    contact.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    print("inside del function ",id)
    delcontact = Contact.objects.get(id=id)
    delcontact.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
  updatecontact = Contact.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'updcontact': updatecontact,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  name = request.POST['name']
  email = request.POST['email']
  member = Contact.objects.get(id=id)
  member.name = name
  member.email = email
  member.save()
  return HttpResponseRedirect(reverse('index'))

def output(request):
   msg1=request.GET.get('buildno')
   msg2=request.GET.get('ipaddress')
   print(msg1,msg2)
   context = {
       'msg1':msg1,
       'msg2':msg2
   }        
   return render(request, 'output.html',context)


def about(request):
    context = {
        'build':"build-Number",
        'ip':"10.30.48.163"
    }
    return render(request,'about.html',context)

def services(request):
   build1=request.GET.get('buildno')
   build2=request.GET.get('ipaddress')
   print(build1,build2)
   return render(request, 'services.html',{'build1':build1,'build2':build2})

def pbx(request):   
    service_name_wsumserver = 'wsumserver'
    wsumserver_instance_ip = ['10.30.48.33','10.30.48.60','10.30.48.194']    
    wsumserver33 = UrlReturn(service_name_wsumserver, wsumserver_instance_ip[0])
    result_wsumserver33= webnagios(wsumserver33)        
    wsumserver60 = UrlReturn(service_name_wsumserver, wsumserver_instance_ip[1])
    result_wsumserver60= webnagios(wsumserver60)        
    wsumserver194 = UrlReturn(service_name_wsumserver, wsumserver_instance_ip[2])
    result_wsumserver194= webnagios(wsumserver194)
       
    # Add WSICP service  
    service_name_WSICP = 'WSICP'
    WSICP_instance_ip = ['10.30.48.148','10.30.48.166','10.30.48.174']    
    WSICP148 = UrlReturn(service_name_WSICP, WSICP_instance_ip[0])
    result_WSICP148= webnagios(WSICP148)
    WSICP166 = UrlReturn(service_name_WSICP, WSICP_instance_ip[1])
    result_WSICP166= webnagios(WSICP166)
    
    context = {
    'result_wsumserver33':result_wsumserver33, 
    'result_wsumserver60':result_wsumserver60, 
    'result_wsumserver194':result_wsumserver194, 
    'result_WSICP148':result_WSICP148, 
    'result_WSICP166':result_WSICP166, 
    }     
    return render(request, 'pbx.html',context)

def contact(request):
    if request.method == "POST":
        Name = request.POST.get('name')            
        Email = request.POST.get('email')
        contact = Contact(name=Name,email=Email,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')
    return render(request,'contact.html')

def web(request):   
    # streams178 = 'http://nagios.beta-wspbx.com/nagios/cgi-bin/statusjson.cgi?query=service&hostname=10.30.48.178&servicedescription=Streams'
    service_name_Streams = 'Streams'
    streams_instance_ip = ['10.30.48.178','10.30.48.183','10.30.48.185']
    streams178 = UrlReturn(service_name_Streams, streams_instance_ip[0])
    result_streams178 = webnagios(streams178)
    
    streams183 = UrlReturn(service_name_Streams, streams_instance_ip[1])
    result_streams183 = webnagios(streams183)

    streams185 = UrlReturn(service_name_Streams, streams_instance_ip[2])
    result_streams185 = webnagios(streams185)
    print("-----------------------inside webfunction")
    print("178:" + result_streams178 + ",183:" + result_streams183,"185:" + result_streams185) 
    # Admin5 Service 
    service_name_Admin5 = 'Admin5'
    Admin5_instance_ip = ['10.30.48.153','10.30.48.154','10.30.48.192']
    Admin5153 = UrlReturn(service_name_Admin5, Admin5_instance_ip[0])
    result_Admin5153 = webnagios(Admin5153)
    
    Admin5154 = UrlReturn(service_name_Admin5, Admin5_instance_ip[1])
    result_Admin5154 = webnagios(Admin5154)

    Admin5192 = UrlReturn(service_name_Admin5, Admin5_instance_ip[2])
    result_Admin5192 = webnagios(Admin5192)   
    
    context = {
        'result_streams178':result_streams178,
        'result_streams183':result_streams183,      
        'result_streams185':result_streams185,      
        'result_Admin5153':result_Admin5153,      
        'result_Admin5154':result_Admin5154,      
        'result_Admin5192':result_Admin5192,      
    }     
    return render(request, 'web.html',context)
    # return render(request, 'web.html',{'result_streams178':result_streams178,'result_streams183':result_streams183,'result_streams185':result_streams185})

# ------------------------- shubham --------------------------------------------------------------------------------------------------------------------
def webnagios(passing_url):    
    request_url = passing_url
    # request_url = 'http://nagios.beta-wspbx.com/nagios/cgi-bin/statusjson.cgi?query=service&hostname=10.30.48.183&servicedescription=Streams'
    username = 'nagiosadmin'
    password = 'nagios@beta'
    session = requests.Session()
    request = session.get(request_url, auth=HTTPBasicAuth(username,password), verify=False) 
    data_json = json.loads(request.text)   
    print("----------------------------")
    print(data_json['data']['service']['plugin_output'])
        
    string = data_json['data']['service']['plugin_output']
    sub_str ="OK" 
    sub_str1 ="ok" 
   
    if (string.find(sub_str) != -1) or (string.find(sub_str1) != -1):
        print("Yes")
        flag = "Running"
        return flag
    else:
        print("No")
        flag = "Not Running" 
        return flag      
 
                
def UrlReturn(service_name,instance_ip):
    return("http://nagios.beta-wspbx.com/nagios/cgi-bin/statusjson.cgi?query=service&hostname=" + instance_ip + "&servicedescription=" + service_name)
      
   
  

    
    
    
    
