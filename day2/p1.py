input = open('input1.txt', 'r')
lines = list(map(str.strip, input.readlines()))

data = {
    'forward' : 0,
    'down' : 0,
    'up' : 0
}
for line in lines:
    (dir,num) = line.split( " " )
    data[dir] = int(num)

#print( data )
result = data['forward'] * ( data['down'] - data['up'])
print( result )