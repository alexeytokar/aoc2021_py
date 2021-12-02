input = open('input1.txt', 'r')
lines = list(map(str.strip, input.readlines()))

data = {
    'forward' : 0,
    'aim' : 0,
    'depth' : 0
}
for line in lines:
    (dir,num) = line.split( " " )
    num = int(num)
    
    if dir == 'down':
        data['aim'] += num
    elif dir == 'up':
        data['aim'] -= num
    else:
        data['forward'] += num
        data['depth'] += data['aim'] * num

print( data )
result = data['depth'] * data['forward']
print( result )