import requests
from bs4 import BeautifulSoup

def update():	
    httpdURL='https://spark.apache.org/downloads.html'
    resp=requests.get(httpdURL)
    if resp.status_code==200:
        print("The news are as follow :-\n")
        
        soup=BeautifulSoup(resp.text,'html.parser')        
        l=soup.find("pre",{"class":"highlight"}) 
        print(l.text)   
        # m = l.find_all("li")[0]
        # print(m)
        
    else:
        print('Error: %s' % resp.status_code)  
        

		
update()
