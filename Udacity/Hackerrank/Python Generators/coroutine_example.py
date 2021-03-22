
def coroutine_example():
    while True:
        x = yield
        print(x)
c = coroutine_example()
c.__next__()
#c.send(10)