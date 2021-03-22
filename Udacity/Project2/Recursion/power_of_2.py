

def power_of_2(number):
    if number == 0:
        return 1
    else:
        output =  2 * power_of_2(number - 1) # return 2 * power_of_2(number - 1)
        return output


value = power_of_2(10000)
print("power_of_2: " + str(value))