input = open('input1.txt', 'r')
line = input.readline()
vals = list(map(int, line.strip().split(",")))

buckets = [0]*9

for v in vals:
    buckets[v] = buckets[v] + 1

for i in range(256):
    tmp = buckets[0]
    for b in range(1,len(buckets)):
        buckets[b-1] = buckets[b]
    buckets[6] = buckets[6] + tmp
    buckets[8] = tmp

print( sum(buckets))