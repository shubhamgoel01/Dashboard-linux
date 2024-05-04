import requests
from bs4 import BeautifulSoup

def update_php(passing_url):  
    resp=requests.get(passing_url)
    if resp.status_code==200:      
        soup=BeautifulSoup(resp.text,'html.parser')        
        l=soup.find("section",{"id":"layout-content"})
        m = l.findAll("h3")[0]
        return(m.text)           
    else:
        return(resp.status_code)          
		
result_php = update_php("https://www.php.net/downloads.php")

print(result_php)