from collections import deque

input = open('input1.txt', 'r')
ls = input.readlines()

rows = 100
cols = 100
matrix = [[0 for i in range(cols)] for j in range(rows)]
basins_idx = [[0] * len(r) for r in matrix]

row = 0
for line in ls:
    matrix[row] = list(map(int,list(line.strip())))
    row += 1

b_idx = 1    
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == 9 or basins_idx[r][c] > 0: 
            continue

        vis = {(r, c)}
        
        q = deque()
        q.append((r, c))
        while q:
            r, c = q.popleft()
            basins_idx[r][c] = b_idx

            for i, j in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if (i, j) in vis: 
                    continue

                if 0 <= i < len(matrix) and 0 <= j < len(matrix[i]):
                    if matrix[i][j] != 9:
                        vis.add((i, j))
                        q.append((i, j))
        b_idx += 1

flat_idx = sum(basins_idx, [])
sizes = [0] * b_idx

for x in flat_idx:
    sizes[x] += 1

sizes = sizes[1:]
sizes.sort()

print(sizes[-1] * sizes[-2] * sizes[-3])