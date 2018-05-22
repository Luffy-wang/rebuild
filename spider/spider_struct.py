from utils import utils
import os
from bs4 import BeautifulSoup
#import MySQLdb
import psycopg2
import redis
import threading
import datetime

class mysqlconn(object):
    def connection(self):
        print('连接到mysql数据库:')
        db=psycopg2.connect(host='localhost',user='postgres',password='123456',dbname='test')
        conn=db.cursor()
        self.sql='insert into problem_problem (title,description,input_description,output_description,_id,time_limit,memory_limit) values(%s,%s,%s,%s,%s,1024,1024);' 
        #for i in range(60):
        #tup1=()
        #self.pool=redis.ConnectionPool(host='localhost',post='6379',db=0)
        r=redis.Redis(host='localhost',port=6379,db=0)
        i=0
        tup1=[]
        while(i<60):
            result=r.hmget(i,'title','Description','Input','Output')
            
            try:
                result[0]=result[0].decode('utf-8')
                result[1]=result[1].decode('utf-8')
                result[2]=result[2].decode('utf-8')
                result[3]=result[3].decode('utf-8')
                result.append(i+1)
            except:
                print(result)
            #return 
            tup1.append(result)
            #print(result)
            r.delete(i)
            
            i+=1
        conn.executemany(self.sql,tup1)
        db.commit()
        db.close()
        return 
class spider_struct(utils):
    #print("please input method")
    def __init__(self):
        self.pool=redis.ConnectionPool(host='localhost',port='6379',db=0)
        #self.method=input("Enter http method:")
        #self.url=input("Enter http url:")

    
    def aa(self,start,end):
        # r=redis.Redis(connection_pool=self.pool)
        # return print(r.get('0').decode('utf-8'))
        for i in range(start,end):
            #start_time=datetime.datetime.now()
            
            r=super(spider_struct,self).request('get','http://poj.org/problem?id='+str(i+1000)+'&lang=zh-CN&change=true')
            
            #end_time=datetime.datetime.now()
            #print(end_time-start_time)

            data=super(spider_struct,self).myparse(r,self.pool)
        #print(data)
        # with open("/tmp/html.html","wb") as f:
        #     f.write(r)
        # print(self.url)



def startcli():
    a=spider_struct()

    # # # #bytes 3000
    start_time=datetime.datetime.now()
    # #a.aa(0,1)
    for i in range(0,60,8):
        t1=threading.Thread(target=a.aa(i,i+8))
        t1.start()

    end_time=datetime.datetime.now()
    print(end_time-start_time)
#test
ac=mysqlconn()
ac.connection()
#startcli()
#test

