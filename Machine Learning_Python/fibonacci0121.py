# 1,1,2,3,5,8,13,21,33

class fibonacci:
    def fibonacci(self, first, second):
        for item in range(10):
            print(str(first) + "," + str(second))
            sum = first + second
            first, second = second, sum

solution = fibonacci()
first = 1
second = 1
solution.fibonacci(first, second)