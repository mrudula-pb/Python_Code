
import csv
import numpy as np

opens = []
x_axis = []

def predict(x_val, coeffs, degree):
        return coeffs[0] * x_val ** 2 + coeffs[1] * x_val + coeffs[2]

with open("AAPL.csv") as readFile:
    reader = csv.reader(readFile)
    next(reader) # start from second row. Ignore the column names(which is in first row)
    for i, row in enumerate(reader):
        opens.append(float(row[1]))
        x_axis.append((i))
    #print(opens)
    #print(x_axis)


degree = 2
coefficients = np.polyfit(x_axis, opens, degree)
print(coefficients)

input_x = int(input("I can predict the future, I will tell you apple stock value if you tell me how many days from"))
print(round(predict(input_x, coefficients, degree), 2))