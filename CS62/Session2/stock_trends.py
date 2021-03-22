import csv
import numpy as np

opens = [] #a list of opening prices for each day since 7/16/18
x_axis = [] #a list of x-values representing the number of days since 7/16/18 e.g. [0, 1, 2......] 

#write a function to take in the x value and returns the y value (x values is days from 7/16/18, y value is opening price for AAPL)
#the function also takes in a list of coefficients. In this case for our linear regression equation y = mx + b (coeffs[0] is m and coeffs[1] is b)
def predict(x_val, coeffs, degree):
        return coeffs[0]*x_val**2 + coeffs[1]*x_val + coeffs[2]
	#to_return = 0
	#for idx, coeff in enumerate(coeffs):
		#to_return += coeff*x_val**(degree-idx)
	#return to_return

	# return coeffs[0]*x_val**(2-0) + coeffs[1]*x_val**(2-1) + coeffs[2]*x_val**(2-2)


#open the csv to read in each "row" of information that we can "iterate" through in our for loop
with open('AAPL.csv') as readFile:
	reader = csv.reader(readFile)
	
	#because the reader is "iterable," we can skip its first row which we know is just titles that we don't care about
	next(reader)

	for i, row in enumerate(reader): #this not only gives each row, but also an index of which row we are on, i
		opens.append(float(row[1]))
		x_axis.append(i)

 #polyfit is a numpy function that takes in 2 lists of data as x values and y values and makes a best fit polynomial to whichever
 #degree you specify (1 degree is a linear regression). So think np.polyfit(x_values, y_values, degree)
degree = 2
coefficients = np.polyfit(x_axis, opens, degree)
print(coefficients)


input_x = int(input("I can prdict the future, I'll tell you apple stock value if you tell me how many days from 7/16/18: "))

print(round(predict(input_x, coefficients, degree), 2))


