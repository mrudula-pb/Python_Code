
# Read in the csv file called “foobar.csv” (in canvas files, and attached herePreview the document)
# and store each row as a data point in the training_dataset
# Ask for a user to input a new xy pair and print out the prediction
# Set up a loop so the user can enter multiple new coordinate pairs
import csv
import math

def store_datapoint():
    with open("foobar.csv") as readFile:
        reader = csv.reader(readFile)
        data_point = list(reader)
        print(data_point)
    return data_point

def euclidean_distance(data1, data2):
    dist = 0.0
    length = len(data1)-1
    for i in range(length):
        dist += (float(data1[i]) - float(data2[i]))**2
    return math.sqrt(dist)

def get_neighbors(train_dataset, test_data, k):
    dists = []
    for train_data in train_dataset:
        dist = euclidean_distance(test_data, train_data)
        dists.append((dist, train_data))

    dists.sort()
    neighbors = []
    for i in range(k):
        neighbors.append(dists[i][1])
    return neighbors

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


training_data = store_datapoint()
new_data_point = []
for i in range(2):
    user_input = input("Input a new xy pair: ")
    new_data_point.append(user_input)
training_data.append(new_data_point)
print(training_data)

print(predict(training_data, new_data_point, 3))



