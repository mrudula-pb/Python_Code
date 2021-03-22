import math

'''
The following dataset is what we call the training dataset,
because we will "train" our algorithm with it. The two 
numbers are x and y coordinates, and the string is the class
that the datapoint at those coordinates belongs to.
Notice the points closer to the origin are 'foos' and further
away are 'bars'
'''
training_data = [[0,0,'foo'], [0,1,'foo'], [1,0,'foo'], [2,1,'foo'], [3,0,'foo'],
[5,4,'bar'], [6,8,'bar'], [7,9,'bar'], [7,7,'bar'], [8,9,'bar']]

#The following function clalculates the Euclidean Distanct between two sets of data.
#In our case, the two sets of data are a pair of the x,y,class lists.
#Note that your data structure could be many data points long, not just 2 like
#in this example (x and y).

#Note also that by using the range(len(data1)-1), we make sure to ignore the last
#position in the data, which in our case is 'foo' or 'bar'
def euclidean_distance(xy1, xy2):
	c_squared = 0.0
	for i in range(len(xy1)-1):
		c_squared += (float(xy1[i]) - float(xy2[i]))**2
	'''
	Another way to write lines 23 and 24 is:
	a = xy1[0]-xy2[0]
	b = xy1[1]-xy2[1]
	c_squared = a**2 + b**2
	'''
	return math.sqrt(c_squared)

#The following function uses the distance function from above to calculate
#each of the distances between the data point we want to classify and each
#of the datasets we have in our training data. Basically, find the closest
#points in the training_data to a new x,y coordinate.
#Next, it sorts the results by the distances calculated (smallest first).
#Finally, it trims the list to only k nearest neighbors
def get_neighbors(train_dataset, test_data, k):
	dists = []
	for train_data in train_dataset:
		dist = euclidean_distance(test_data, train_data)
		dists.append((dist,train_data))
	
	dists.sort()
	neighbors = []
	for i in range(k):
		neighbors.append(dists[i][1])
	return neighbors

#The following function uses the get_neighbors function from above, then
#figures out which class has the most neighbors in it to predict the
#most likely class that a new dataset belongs in. Basically, given the
#closest neighbors to this new coordinate, how many are 'foo' and how
#many are 'bar,' this new coordinate probably belongs to the majority.
def predict(train_dataset, test_data, k):
	neighbors = get_neighbors(train_dataset, test_data, k)
	output_values = []
	count_foo = 0
	count_bar = 0
	for n in neighbors:
		if n[-1] == 'foo':
			count_foo += 1
		else:
			count_bar += 1
	if count_foo > count_bar:
		prediction = 'foo'
	elif count_foo < count_bar:
		prediction = 'bar'
	else:
		prediction = 'Could not classify'
	return prediction

print(predict(training_data, [20,10], 3))

