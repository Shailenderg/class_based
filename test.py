import requests
from bs4 import BeautifulSoup
import webbrowser 
url = 'https://www.geeksforgeeks.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

urls = []
for link in soup.find_all('a'):
    urls.append(link.get('href'))
# import ipdb;ipdb.set_trace()
urls.pop(0)
# print(urls) \
cnt=0
def get_info(data):

#    for i in urls:
#        cnt+=1
#        url1 = i
#        print(cnt)
       reqs = requests.get(data)
       soup1 = BeautifulSoup(reqs.text, 'html.parser')

       df = soup.find('div', class_="col-11 col-sm-9 col-lg-9 mx-auto courseCard")
    #    df1 = soup.find('div', class_="container-fluid bg-light").find_all('div')
    #    df2 = soup.find('div', class_="right-wrap_top").find('span') 
    #    df3 = soup1.find('span', class_="read-more").a.href
    #    df4 = soup1.find('div', class_="a-wrapper")
    #    if df4==None:
         
       print(df)
       
       
  
class StoreInfo():
    import ipdb;ipdb.set_trace()
    for link in urls:
     storedinfo = get_info(link)
    print(storedinfo) 