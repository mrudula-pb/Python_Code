
def countdown(n, test):
    while n > 0:
        test(n)
        n -= 1
    print("finishing now")

def divisibleBy(divisor, num):
    if (num % divisor == 0):
    	print(f'{num} is divisible by {divisor}')
    else:
    	print(f'{num} is not divisible by {divisor}')

even_odd_test = lambda x : divisibleBy(2, x)
countdown(10,even_odd_test)