import urllib3
from bs4 import BeautifulSoup
import redis
import threading



k=0
class utils(object):
    
    def request(self,method,url):
        
        http=urllib3.PoolManager()
        r=http.request(method,url)
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

        # for i in p:
        #     print(i)
        # print('--------------')
        # for i in div:
        #     print(i)
        # print('--------------')
        # for i in sio:
        #     print(i)
        # return 
        # # print(p[0].string)
        # # return 
        # tmp=[None]
        # for i in range(6):
        #     tmp.append(p[i].string)
        #     if(i<3):
        #         tmp.append(div[i].string)
        #     if(i>2 and i<5):
        #         tmp.append(sio[i-3].string)
        #     if(i==5):
        #         tmp.append(div[3])
        
        # for i in tmp:
        #     print(i)
        
        # for i in div:
        #     #if(i['class']=='ptx'):
        #     print(i)
        #     #print(j.string)
        # for j in sio:
        #     print(j.string)
        #print(p)
        # tag1=p[1].contents[0]
        # tag=p[0].contents[1]
        # print(tag.contents[0])
        # print(tag1)
        # print(h3[0].contents[0])
        
        
        #p pre class=ptx
        #get_text()
