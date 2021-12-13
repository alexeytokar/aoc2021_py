dots = set()

data = open('input1.txt', 'r').read()
fill, folds = data.split("\n\n")

for line in fill.splitlines():
    x, y = map(int, line.split(","))
    dots.add((x, y))

prefixLen = len( "fold along " )
for line in folds.splitlines():
    line = line[prefixLen:]
    axis, num = line.split("=")
    num = int(num)
    if axis == "x":
        dots = {(x if x < num else num - (x - num), y) for x, y in dots}
    else:
        dots = {(x, y if y < num else num - (y - num)) for x, y in dots}

matrix = [[' ' for i in range(100)] for j in range(10)]
for x,y in dots:
    matrix[y][x] = '#'

def mat( matrix ):
    for row in matrix:
        print(''.join(row))

mat( matrix )