input = open('input1.txt', 'r')
lines = list(map(int,map(str.strip, input.readlines())))

cnt = 0
prevDepth = lines[0]
for depth in lines[1:]:
    if depth > prevDepth:
        cnt += 1

    prevDepth = depth

print( cnt )