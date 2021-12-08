input = open('input1.txt', 'r')
lines = input.readlines()
cnt = 0;

def mis(o,num):
    return list(set(list(o))^set(list(num)))

def cnt(o,num):
    l = list(o)
    n = list(num)

    return len(list(set(l).intersection(n))) == len(num)

ssssum = 0
for line in lines:
    p = line.strip().split(" | ")
    right = p[1].split( " " )
    left = p[0].split( " " )

    nums = [""]*10
    ov = []
    size2idx = {2:1,3:7,4:4,7:8}
    for li in left:
        li = ''.join(sorted(li))
        if len(li) in size2idx:
            nums[size2idx[len(li)]] = li
        else:
            ov.append(li)

    for o in ov:
        if len(o) == 5:
            if cnt(o,nums[1]):
                nums[3] = o
            elif cnt(o,mis(nums[4],nums[1])):
                nums[5] = o
            else:
                nums[2] = o
    
    for o in ov:
        if len(o) == 6:
            if cnt(o,nums[3]):
                nums[9] = o
            elif cnt(o,nums[5]):
                nums[6] = o
            else:
                nums[0] = o

    maps = {}
    for n in range(len(nums)):
        maps[nums[n]] = n


    tt = ""
    for r in right:
        s = ''.join(sorted(r))
        tt = tt + str(maps[s])
    ssssum = ssssum + int(tt)





print( ssssum )