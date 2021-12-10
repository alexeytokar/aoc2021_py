input = open('input1.txt', 'r')

open = "([{<"
close = ")]}>"
scores = [3,57,1197,25137]


total = 0
for line in input.readlines():
    stack = []

    for c in list(line.strip()):
        if c in open:
            stack.append(c)
        elif c in close:
            idx = close.find(c)
            el = stack.pop()
            if el != open[idx]:
                total += scores[idx]
                break

print( total )
