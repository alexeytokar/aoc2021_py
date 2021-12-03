input = open('input1.txt', 'r')
lines = list(map(str.strip, input.readlines()))

total = len(lines)

result = ""
for i in range(len(lines[0])):
    ones = sum(int(line[i]) for line in lines)
    result += "1" if ones > total/2 else "0"

print( int(result,2) * (2**len(lines[0]) - 1 - int(result,2)) )
