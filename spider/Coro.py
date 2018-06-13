def fib(n):
    index=0
    a=0
    b=1
    while index<n:
        yield b
        a,b=b,a+b
        index+=1


def fib_with_coro(n):
    index=0
    a=0
    b=1
    while index<n:
        cnt=yield b
        print('do something ',cnt)
        a,b=b,a+b
        index+=1

print("start")

fib_with=fib_with_coro(20)
fib_item=next(fib_with)
a=0
while True:
    print(fib_item)

    try:
        fib_item=fib_with.send(a)
    except StopIteration:
        break
    a+=1