from collections import defaultdict,  deque

input = open('input1.txt', 'r')

adj = defaultdict(list)
for line in input.readlines():
    (a,b) = line.strip().split('-')
    adj[a].append(b)
    adj[b].append(a)

START_P = 'start'
END_P = 'end'

small = set([START_P])
start = (START_P, small, None)
count = 0
q = deque([start])
while q:
    pos, small, isok = q.pop()
    if pos == END_P:
        count += 1
        continue

    for y in adj[pos]:
        if y not in small:
            new = set(small)

            if y.lower() == y:
                new.add(y)

            q.append( (y, new, isok) )

        elif y in small and isok is None:
            if y not in [START_P, END_P]:
                q.append( (y, small, y) )


print(count)