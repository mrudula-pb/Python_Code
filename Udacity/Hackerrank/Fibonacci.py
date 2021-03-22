
def fibonacci():
    first,second = 0,1
    for i in range(10):
        third = first + second
        yield second
        first = second
        second = third

value = fibonacci()
for n in fibonacci():
    print(n)


# print(value.__next__())
# print(value.__next__())
# print(value.__next__())
# print(value.__next__())
# print(value.__next__())
# print(value.__next__())
# print(value.__next__())
# print(value.__next__())
# print(value.__next__())
# print(value.__next__())
# #print(value.__next__())
#print(value.__next__())