# streams178 = 'http://nagios.beta-wspbx.com/nagios/cgi-bin/statusjson.cgi?query=service&hostname=10.30.48.178&servicedescription=Streams'
admin153 = 'http://nagios.beta-wspbx.com/nagios/cgi-bin/statusjson.cgi?query=service&hostname=10.30.48.153&servicedescription=Admin5'
ip = '10.30.48.153'
name="Admin5"
def yoo(streams178,number):
    return("http://nagios.beta-wspbx.com/nagios/cgi-bin/statusjson.cgi?query=service&hostname="+ip+"&servicedescription="+name)    


print("Lets Go")
a = yoo(ip,name)
print(admin153)
print(a)
print("\n")
if (a == admin153):
    print("OK")
else:
    print("Failed")



