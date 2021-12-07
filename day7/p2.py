input = open('input1.txt', 'r')
line = input.readline()
vals = list(map(int, line.strip().split(",")))

result = float('inf')
for i in vals:
    fv = []
    for x in vals:
        dist = abs( x - i )
        
        fv.append( dist * (dist + 1) // 2 )
    result = min( result, sum(fv))

print( result)
