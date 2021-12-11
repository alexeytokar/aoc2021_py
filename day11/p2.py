input = open('input1.txt', 'r')

def mat( matrix ):
    for row in matrix:
        print(row)

rows = 10
cols = 10
matrix = [[0 for i in range(cols)] for j in range(rows)]

lines = input.readlines()
row = 0
for line in lines:
    matrix[row] = list(map(int,list(line.strip())))
    row = row + 1

mat( matrix )

flashed = [[0] * len(r) for r in matrix]

def flash(matrix, r, c):
    global flashed
    flashed[r][c] = 1
    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            if i == r and j == c: 
                continue

            if 0 <= i < len(matrix) and 0 <= j < len(matrix[i]):
                matrix[i][j] += 1
                
                if matrix[i][j] == 10:
                    flash(matrix, i, j)
                    matrix[i][j] += 1
n = 0

while True:
    n += 1

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            matrix[r][c] += 1

            if matrix[r][c] == 10:
                flash(matrix, r, c)
                matrix[r][c] += 1

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] > 9:
                matrix[r][c] = 0

    if all(map(all, flashed)):
        print(n)
        break
    
    flashed = [[0] * len(r) for r in matrix]