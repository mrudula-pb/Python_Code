# Program to add two matrices using nested loop

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

length_y = len(Y[0])
print(length_y)

for i in range(len(X)):
    for j in range(len(Y)):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)