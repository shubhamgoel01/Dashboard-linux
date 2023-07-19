import requests
from bs4 import BeautifulSoup

def update():	
    httpdURL='https://www.openssl.org/source/'
    resp=requests.get(httpdURL)
    if resp.status_code==200:
        print("Successfully opened the web page")
        print("The news are as follow :-\n")
        
        soup=BeautifulSoup(resp.text,'html.parser')        
        # l=soup.find("div",{"class":"blog-index"})
        l=soup.find("table")
        m = l.findAll("tr")[2]
        n = m.findAll("td")[2]        
        print(n.text)
        # m = l.findAll("tr")[5]
        # print(m.text)           
    else:
        print('Error: %s' % resp.status_code)   
        

		
update()
