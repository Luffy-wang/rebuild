import urllib3
from bs4 import BeautifulSoup
class utils(object):
    def request(self,method,url):
        http=urllib3.PoolManager()
        r=http.request(method,url)
        return r.data
    def myparse(slef,html):
        soup=BeautifulSoup(html,"html.parser")
        h3=soup.find_all("h3")
        
        p=soup.find_all("p")

        print(h3)
        print(p)
        # tag1=p[1].contents[0]
        # tag=p[0].contents[1]
        # print(tag.contents[0])
        # print(tag1)
        # print(h3[0].contents[0])
