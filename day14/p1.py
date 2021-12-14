dots = set()

lines = list(map(lambda x:x.strip(),open('input1.txt', 'r').readlines()))

initial = lines[0]
formula = lines[2:]
lets = {}

tmap = {}
for i in range(len(initial)-1):
    if initial[i] not in lets:
        lets[initial[i]] = 1
    else:
        lets[initial[i]] += 1
    if initial[i:i+2] not in tmap:
        tmap[initial[i:i+2]] = 1
    else:
        tmap[initial[i:i+2]] += 1

if initial[len(initial)-1] not in lets:
    lets[initial[len(initial)-1]] = 1
else:
    lets[initial[len(initial)-1]] += 1

rep = {}
for i in formula:
    k,v = i.split( ' -> ' )
    rep[k] = v

for i in range(10):
    new = dict(tmap)
    for k in rep:
        v = rep[k]
        cnt = tmap[k] if k in tmap else 0
        if cnt == 0:
            continue
        
        if v not in lets:
            lets[v] = 0
        lets[v] += cnt
            
        new[k] -= cnt
        k1 =k[0]+v 
        if k1 in new:
            new[k1] += cnt
        else:
            new[k1] = cnt

        k2 = v + k[1] 
        if k2 in new:
            new[k2] += cnt
        else:
            new[k2] = cnt

        #print( k, v, cnt, new )

    tmap = dict(new)


print(lets)
mn = 9999999999999999
mx = -1
for k in lets:
    mn = min( mn, lets[k])
    mx = max( mx, lets[k])


print( mx - mn )