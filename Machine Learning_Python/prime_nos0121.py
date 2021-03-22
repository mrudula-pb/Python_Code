class prime_numbers:
    def list_prime_nos(self, number):
        for dividend in range(3, number):
            for divisor in range(2, dividend):
                if dividend > divisor and dividend % divisor == 0:
                    break
            else:
                print(str(dividend) + " IS  PRIME")


solution = prime_numbers()
number = 20
solution.list_prime_nos(number)