rows = 14
cols = 4
array_2d = [[0 for _ in range(cols)] for _ in range(rows)]

# Print the 2D array
array_2d[0][1] = 93
for row in array_2d:
    print(row)