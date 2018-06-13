import asyncio
import aiohttp
from bs4 import BeautifulSoup

# async def myfun(i):
#     print('start {}th'.format(i))
#     await asyncio.sleep(1)
#     print('finish {}th'.format(i))

# loop=asyncio.get_event_loop()

'''
第一种一般实现
myfun_list=(myfun(i) for i in range(10))
loop.run_until_complete(asyncio.gather(*myfun_list))
'''

'''
第二种一般实现
myfun_list=[asyncio.ensure_future(myfun(i)) for i in range(10)]
loop.run_until_complete(asyncio.wait(myfun_list))
'''

#-----------------------------------------------------------------------#

#实现单线程的异步爬虫

'''
    想要异步运行的函数，在定义时要加上async
'''

async def get_title(i):
    url='https://movie.douban.com/top250?start={}&filter='.format(i*25)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            text=await resp.text()
            print('start',i)
    soup=BeautifulSoup(text,'html.parser')
    lis=soup.find('ol',class_='grid_view').find_all('li')
    for li in lis:
        title=li.find('span',class_='title').text
        print(title)
# loop=asyncio.get_event_loop()
# ful_list=(get_title(i) for i in range(10))
# loop.run_until_complete(asyncio.gather(*ful_list))   

# quick_sort
import random
import datetime

def swap(array,index1,index2):
    tmp=array[index1]
    array[index1]=array[index2]
    array[index2]=tmp

def partion(array,start,end,length):
    if start<0 or end>length :
        return 0
    index=random.randint(start,end)
    swap(array,index,end)
    index=start
    small=start-1
    while index<end:
        if array[index]<array[end]:
            small+=1
            if small!=index:
                swap(array,index,small)
        index+=1
    small+=1
    swap(array,small,end)
    return small
class Stack: 
    """模拟栈""" 
    def __init__(self): 
        self.items = [] 

    def isEmpty(self): 
        return len(self.items)==0  

    def push(self, item): 
        self.items.append(item) 

    def pop(self): 
        return self.items.pop()  

    def peek(self): 
        if not self.isEmpty(): 
            return self.items[len(self.items)-1] 

    def size(self): 
        return len(self.items) 


def quick_sort(nums,start,end,length):

    # index=partion(array,start,end,length)
    # if index>start:
    #     quick_sort(array,start,index-1,length)
    # if index<end:
    #     quick_sort(array,index+1,end,length)
def main():
    array=[]
    for i in range(100000):
        array.append(random.randint(0,100))
    #print(array)
    start_time=datetime.datetime.now()
    quick_sort(array,0,99999,100000)
    end_time=datetime.datetime.now()
    print(end_time-start_time)
    #print(array)

main()