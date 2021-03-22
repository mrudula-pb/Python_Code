
print('Hello World!')
# --------------------
var = input("What's your name: ")
print(var)
# -------------------
x = int(input("Enter first number: "))
y = int(input('Enter second number: '))
print(x * y)
# ------------------
test = input("Guess what word I'M THINKING ABOUT: ")
if test == 'T':
    print('Good!')
elif test == 't':
    print("BAD!")
else:
    print("Wrong")
# -----------------
if True:
    print("True")
else:
    print("False")

#----------------------
# declare list
lst = []
print(lst)
lst.append(2)
print(lst)
my_list = [1,2,3]

for item in my_list:
    print(item)
    print(item * 2)

# declare dict
dict = {}
next_dict = {'pen':'bic pen', 'paper': 'acme'}

for item, value in next_dict.items():
    #print(item)
    #print(next_dict[item])
    print(item + ':' + value)

# while loop

# for loop is used when you know when there are certain no: of loops to run
# while loop is used when you have a condition

try: # if this fails, go to except; if this is success, go to else
    var = 100/1
except: # if this doesn't work then go to else
    print("No can do")
else:
    print(var)
print('Done')