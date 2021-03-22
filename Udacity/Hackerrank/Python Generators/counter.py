
def counter(string):
    count = 0
    try:
        while True:
            item = yield
            if isinstance(item, str):
                if item in string:
                    count += 1
                    print(item)
                else:
                    print("No Match")
            else:
                print('Not a string')
    except GeneratorExit:
        print(count)

c = counter("California")
c.__next__()
c.send("Cali")
c.send("nia")
c.send(1234)
c.send("sdasd")