# Define two matrices X and Y
X = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
Y = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]

# Initialize the result matrix with zeros
result = [[0, 0, 0, 0] for _ in range(len(X))]

# Iterate through rows of X
for i in range(len(X)):
    # Iterate through columns of Y
    for j in range(len(Y[0])):
        # Iterate through rows of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

# Print the result
for r in result:
    print(r)
