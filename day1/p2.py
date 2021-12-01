file1 = open('input2.txt', 'r')
lines = list(map(int,map(str.strip, file1.readlines())))

cnt = 0
prevDepth = sum(lines[0:3])
for i in range(1,len(lines)-2):
    depth = sum(lines[i:(i+3)])
    
    if depth > prevDepth:
        cnt += 1

    prevDepth = depth

print( cnt )