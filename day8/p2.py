input = open('input1.txt', 'r')
lines = input.readlines()
cnt = 0;

def mis(o,num):
    return list(set(list(o))^set(list(num)))

def cnt(o,num):
    l = list(o)
    n = list(num)

    return len(list(set(l).intersection(n))) == len(num)

print(cnt("bcdefg","bcdef"))

ssssum = 0
for line in lines:
    p = line.strip().split(" | ")
    right = p[1].split( " " )
    left = p[0].split( " " )

    lefts = []
    for l in left:
        lefts.append( ''.join(sorted(l)) )

    nums = [""]*10
    ov = []
    for li in lefts:
        if len(li) == 2:
            nums[1] = li
        elif len(li) == 3:
            nums[7] = li
        elif len(li) == 4:
            nums[4] = li
        elif len(li) == 7:
            nums[8] = li
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
            print(o)
            if cnt(o,nums[3]):
                print(9)
                nums[9] = o
            elif cnt(o,nums[5]):
                print(6)
                nums[6] = o
            else:
                print(0)
                nums[0] = o
            print(nums)
            print('--')

    maps = {}
    for n in range(len(nums)):
        maps[nums[n]] = n


    tt = ""
    for r in right:
        s = ''.join(sorted(r))
        tt = tt + str(maps[s])
    print( int(tt) )
    ssssum = ssssum + int(tt)





print( ssssum )