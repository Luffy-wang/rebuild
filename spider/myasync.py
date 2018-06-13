import asyncio
import threading

@asyncio.coroutine
# def hello():
#     print('hi ',threading.currentThread())
#     r=yield from asyncio.sleep(1)
#     print('bye',threading.currentThread())

def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


'''
    在python3.5中，@asyncio.coroutine被asyc函数定义头代替
                    yield from 被await代替
'''

loop=asyncio.get_event_loop()
tasks=[wget(host) for host in ['www.baidu.com','www.sina.com.cn','www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


'''

    aiohttp是基于asyncio实现的http框架


'''
