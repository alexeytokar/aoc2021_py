input = open('input1.txt', 'r')
def mat( matrix ):
    for row in matrix:
        print(row)

rows = 100
cols = 100
matrix = [[0 for i in range(cols)] for j in range(rows)]

lines = input.readlines()
row = 0
for line in lines:
    matrix[row] = list(map(int,list(line.strip())))
    row = row + 1

sum = 0
for i in range( rows ):
    for j in range( cols ):
        isMin = True
        
        if j > 0 and matrix[i][j-1] <= matrix[i][j]:
            isMin = False
        if j < (cols - 1) and matrix[i][j+1] <= matrix[i][j]:
            isMin = False
        if i > 0 and matrix[i-1][j] <= matrix[i][j]:
            isMin = False
        if i < (rows - 1 ) and matrix[i+1][j] <= matrix[i][j]:
            isMin = False
        if isMin:
            sum = sum + matrix[i][j] + 1

print( sum )