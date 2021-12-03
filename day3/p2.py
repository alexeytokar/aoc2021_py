input = open('input1.txt', 'r')
lines = list(map(str.strip, input.readlines()))

pattern = ""
for i in range(len(lines[0])):
    ooo = 0
    total = 0
    for line in lines:
        if line.startswith(pattern):
            total += 1
            ooo += int(line[i])

    
    pattern += "0" if ooo < (total/2) else "1"


r1 = int(pattern,2)



pattern = ""
lastLine = ""
for i in range(len(lines[0])):
    ooo = 0
    total = 0
    for line in lines:
        if line.startswith(pattern):
            total += 1
            ooo += int(line[i])
            lastLine = line

    if total == 1:
        pattern = lastLine
    else:
        pattern += "0" if ooo >= (total/2) else "1"
        

r2 = int(pattern,2)

print( r1 * r2 )