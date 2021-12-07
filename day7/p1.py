input = open('input1.txt', 'r')
line = input.readline()
vals = list(map(int, line.strip().split(",")))

result = float('inf')
for i in vals:
    fv = []
    for x in vals:
        fv.append( abs( x - i ) )
    result = min( result, sum(fv))

print( result)
