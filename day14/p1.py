dots = set()

lines = list(map(lambda x:x.strip(),open('input1.txt', 'r').readlines()))

initial = lines[0]
formula = lines[2:]


tmap = {}
for i in range(len(initial)-1):
    tmap[initial[i:i+2]] = tmap.get(initial[i:i+2],0) + 1

lets = {}
for i in range(len(initial)):
    lets[initial[i]] = lets.get(initial[i],0) + 1

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
        
        lets[v] = lets.get( v, 0 ) + cnt
            
        new[k] -= cnt
        k1 =k[0]+v 
        new[k1] = new.get( k1, 0 ) + cnt

        k2 = v + k[1] 
        new[k2] = new.get( k2, 0 ) + cnt

        #print( k, v, cnt, new )

    tmap = dict(new)



mn = float('inf')
mx = -1
for k in lets:
    mn = min( mn, lets[k])
    mx = max( mx, lets[k])


print( mx - mn )