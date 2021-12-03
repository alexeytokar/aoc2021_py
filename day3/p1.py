input = open('input1.txt', 'r')
lines = list(map(str.strip, input.readlines()))


total = len(lines)

result = ""
for i in range(len(lines[0])):
    ones = 0
    for line in lines:
        ones += int(line[i])
    result += "1" if ones > total/2 else "0"


print( result )

r1 = int(result,2)
r2 = 2**len(lines[0]) - 1 - r1
print( r1 )
print( r2 )

print( r1 * r2 )
