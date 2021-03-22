

def sum_x(x):
    sum_x = 0
    for i in range(len(x)):
        sum_x += x[i]
    return sum_x

x = [1,2,3,4,5]
value = sum_x(x)
print(value)