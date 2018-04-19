from utils import utils
import os
from bs4 import BeautifulSoup
class spider_struct(utils):
    #print("please input method")
    def __init__(self):
        self.method=input("Enter http method:")
        self.url=input("Enter http url:")
    def aa(self):
        r=super(spider_struct,self).request(self.method,self.url)
        data=super(spider_struct,self).myparse(r)
        #print(data)
        # with open("/tmp/html.html","wb") as f:
        #     f.write(r)
        # print(self.url)

a=spider_struct()
a.aa()