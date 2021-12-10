input = open('input1.txt', 'r')

open = "([{<"
close = ")]}>"
scores = [3,57,1197,25137]
additions = [1,2,3,4]


result = []
for line in input.readlines():
    
    stack = []
    correct = True
    for c in list(line.strip()):
        if c in open:
            stack.append(c)
        elif c in close:
            idx = close.find(c)
            el = stack.pop()
            if el != open[idx]:
                correct = False
                break

    if correct:
        total = 0    
        stack.reverse()
        for el in stack:
            total = total * 5 + additions[open.find(el)]
        result.append( total )

result.sort()
print( result[len(result)//2] )


