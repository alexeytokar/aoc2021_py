input = open('input1.txt', 'r')

def mat( matrix ):
    cnt = 0;
    for row in matrix:
        # print(row)
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
            matrix[i][x1] = matrix[i][x1] + 1

    elif y1 == y2:
        for i in range( min(x1,x2), max(x1,x2) + 1 ):
            matrix[y1][i] = matrix[y1][i] + 1

    else:
        dx = 1 if x1 < x2 else -1;
        dy = 1 if y1 < y2 else -1;
        
        for i in range( 0, max(x1,x2)-min(x1,x2)+1 ):
            matrix[y1+dy*i][x1+dx*i] = matrix[y1+dy*i][x1+dx*i] + 1

    line = input.readline()

mat( matrix )
