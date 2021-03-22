
def even_integers_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
integers = even_integers_generator(10)
# print(integers.__next__())
# print(integers.__next__())
# print(integers.__next__())
# print(integers.__next__())
# print(integers.__next__())

# for n in integers:
#     print(n)
#
# for i in even_integers_generator(10):
#     print(i)

for n in (i for i in range(10)):
    print(n)

print(max(i for i in range(10)))