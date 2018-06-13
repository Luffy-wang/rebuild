import urllib3
from bs4 import BeautifulSoup
import redis
import threading
import logging


k=0

logging.basicConfig(filename='request.log')
class utils(object):
    
    def request(self,method,url):
        
        http=urllib3.PoolManager()
        r=http.request(method,url)
        if r.status != 200:
            logging.error(url+' status:'+str(r.status))
        else:
            return r.data
    def myparse(self,html,redisconn):
        global k
        lock=threading.Lock()
        soup=BeautifulSoup(html,"html.parser")
        #h3=soup.find_all("h3")
        
        p=soup.find_all(attrs={'class':'pst'})
        div=soup.find_all(attrs={'class':'ptx'})
        sio=soup.find_all(attrs={'class':'sio'})
        ptt=soup.find_all(attrs={'class':'ptt'})
        #return print(ptt[0].get_text())
        r=redis.Redis(connection_pool=redisconn)
        #r.set('name','test')
        #print(r.get('name'))
        #return
        lock.acquire()
        try:
            d={}
            d={'title':ptt[0].get_text()}
            for i in range(6):
                #print(p[i].string)
                if(i<3):
                    d[p[i].string]=div[i].get_text()
                if(i>2 and i<5):
                    d[p[i].string]=sio[i-3].get_text()
                if(p[i].string=='Hint'):
                    d[p[i].string]=div[3].get_text()
            r.hmset(k,d)
            r.incr('mount')
            # print(r.get(k))
            # r.delete(k)
            k+=1
            #r.publish(i,d)
        finally:
            lock.release()
        return

# bc=utils()
# bc.request('get','http://poj.org/problem?id=1000&lang=zh-CN&change=true')