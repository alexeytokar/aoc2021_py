input = open('input1.txt', 'r')

def mat( matrix ):
    cnt = 0;
    for row in matrix:
        print(row)
        for e in row:
            if e > 1:
                cnt = cnt + 1 
    print( cnt )


size = 1000
line = input.readline()

matrix = [[0 for i in range(size)] for j in range(size)]

while line:
    parts = line.split( ' -> ' )
    (x1,y1) = tuple(list(map(int,parts[0].split(","))))
    (x2,y2) = tuple(list(map(int,parts[1].split(","))))

    if x1 == x2:
        for i in range( min(y1,y2), max(y1,y2) + 1 ):
            matrix[x1][i] = matrix[x1][i] + 1

    elif y1 == y2:
        for i in range( min(x1,x2), max(x1,x2) + 1 ):
            val = int(matrix[i][y1] + 1)
            matrix[i][y1] = val
            
    line = input.readline()

mat( matrix )
