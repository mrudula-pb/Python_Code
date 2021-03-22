
# def bare_bones():
#     print("My first Coroutine")
#     try:
#         while True:
#             value = (yield)
#             print(value)
#     except GeneratorExit:
#         print("Exiting Coroutine...")
#
# coroutine = bare_bones()
# next(coroutine) #coroutine.__next__()
# coroutine.send("First Value")
# coroutine.send("Second Value")
# coroutine.close()

# def filter_line(num):
#     print('num: ', num)
#     while True:
#         line = (yield)
#         if num in line:
#             print(line)
#
# coroutine = filter_line("33")
# next(coroutine)
# coroutine.send("Jessica, age:24")
# coroutine.send("Marco, age:33")
# coroutine.send("Filipe, age:55")

# Applying Several Breakpoints: Multiple yield statements can be sequenced together in the same individual coroutine:
# def joint_print():
#     print('First Coroutine')
#
#     while True:
#         part_1 = (yield)
#         part_2 = (yield )
#         print("{} : {}".format(part_1,part_2))
#
#
# coroutine = joint_print()
# next(coroutine)
# coroutine.send("So Far")
# coroutine.send("So Good")

# The StopIteration Exception: After a coroutine is closed, calling send() again will generate a StopIteration exception:
# def test():
#     while True:
#         value = (yield)
#         print(value)
#
# try:
#     coroutine = test()
#     next(coroutine)
#     coroutine.close()
#     coroutine.send("So Good")
# except StopIteration:
#     print("Done with the basics")

# Coroutines with Decorators



# Coroutines pipelines
def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start

def producer(cor):
    n = 1
    while n < 100:
        cor.send(n)
        n = n * 2

@coroutine
def my_filter(num, cor):
    while True:
        n = (yield)
        if n < num:
            cor.send(n)

@coroutine
def printer():
    while True:
        n = (yield)
        print(n)

prnt = printer()
filt = my_filter(50, prnt)
producer(filt)



