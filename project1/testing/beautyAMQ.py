import requests
from bs4 import BeautifulSoup

resp = requests.get("https://activemq.apache.org/components/classic/download/")
if resp.status_code==200:
    soup=BeautifulSoup(resp.text,'html.parser') 
    l=soup.find("h4") 
    # l=soup.find_all("h4",{"id":"activemq"}) 
    # m = l.find("h4")
    print("yes")
    print(l.text)
    # print(m)
else:
    print("no")
    
# soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
# print(soup.prettify())


# def update_java(passing_url): 
#     resp=requests.get(passing_url)
#     if resp.status_code==200:      
#         soup=BeautifulSoup(resp.text,'html.parser')        
#         l=soup.find("ul",{"class":"cta-list"})    
#         m = l.find_all("li")[0]
#         n = m.find("p")        
#         return(n.text)        
#     else:
#         return(resp.status_code) 