input = open('input1.txt', 'r')
lines = input.readlines()
cnt = 0;

def mis(o,num):
    return list(set(list(o))^set(list(num)))

def cnt(o,num):
    l = list(o)
    n = list(num)

    return len(list(set(l).intersection(n))) == len(num)

def code2int( parts, codemap ):
    tt = ""
    for r in parts:
        s = ''.join(sorted(r))
        tt = tt + str(codemap[s])
    return int(tt)

def nums2map(nums):
    maps = {}
    for n in range(len(nums)):
        maps[nums[n]] = n

    return maps

def process6( input, nums ):
    for o in input:
        if len(o) == 6:
            if cnt(o,nums[3]):
                nums[9] = o
            elif cnt(o,nums[5]):
                nums[6] = o
            else:
                nums[0] = o

    return nums

def process5(input, nums):
    for o in input:
        if len(o) == 5:
            if cnt(o,nums[1]):
                nums[3] = o
            elif cnt(o,mis(nums[4],nums[1])):
                nums[5] = o
            else:
                nums[2] = o

    return nums  

def processSimplest( input ):
    nums = [""]*10
    size2idx = {2:1,3:7,4:4,7:8}
    for li in input:
        if len(li) in size2idx:
            nums[size2idx[len(li)]] = li

    return nums

def splitInput( input ):
    p = input.strip().split(" | ")
    right = p[1].split( " " )
    left = p[0].split( " " )

    return (left, right)

def prepareData( input ):
    ov = []
    for l in input:
        ov.append( ''.join(sorted(l)) )

    return ov

result = 0
for line in lines:
    (left,right) = splitInput( line )
    
    ov = prepareData( left )
    
    nums = processSimplest( ov )
    nums = process5( ov, nums )
    nums = process6( ov, nums )

    maps = nums2map(nums)
    result = result + code2int( right, maps )

print( result )