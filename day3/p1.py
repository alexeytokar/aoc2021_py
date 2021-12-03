input = open('input1.txt', 'r')
lines = list(map(str.strip, input.readlines()))


result = None
total = len(lines)
gamma = [0]*len(lines[0])

for line in lines:
    for i in range(len(line)):
        gamma[i] += int(line[i])

result = ""
result_r = ""
for g in gamma:
    result += "1" if g > total/2 else "0"
    result_r += "1" if g < total/2 else "0"

print( gamma )
print( result )

print( int(result,2) )
print( int(result_r,2) )

print(int(result,2) * int(result_r,2))