input = open('input1.txt', 'r')
lines = list(map(str.strip, input.readlines()))


result = None

pattern = ""
for i in range(len(lines[0])):
    ooo = 0
    total = 0
    for line in lines:
        if line.startswith(pattern):
            total += 1
            # print(line)
            ooo += int(line[i])

    
    if ooo < (total/2):
        pattern += "0"
    else:
        pattern += "1"

    # print("---")
    # print( ooo )
    # print( pattern )

r1 = int(pattern,2)



pattern = ""
lastLine = ""
for i in range(len(lines[0])):
    ooo = 0
    total = 0
    for line in lines:
        if line.startswith(pattern):
            total += 1
            print(line)
            ooo += int(line[i])
            lastLine = line

    if total == 1:
        pattern = lastLine
    else:
        if ooo >= (total/2):
            pattern += "0"
        else:
            pattern += "1"

    print("---")
    print( ooo )
    print( pattern )


r2 = int(pattern,2)
print('000----')
print( pattern )

print( r1 * r2 )