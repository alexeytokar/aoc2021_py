def extractPart(o,num):
    return set(o)^set(num)

def hasMatch(o,num):
    return len(set(o).intersection(list(num))) == len(num)

def code2int( parts, codemap ):
    numstr = ""
    for r in parts:
        s = ''.join(sorted(r))
        numstr = numstr + str(codemap[s])
    return int(numstr)

def nums2map(nums):
    return { nums[n] : n for n in range(len(nums))}

def processLen6( input, nums ):
    for o in filter( lambda l: len(l) == 6, input):
            if hasMatch(o,nums[3]):
                nums[9] = o
            elif hasMatch(o,nums[5]):
                nums[6] = o
            else:
                nums[0] = o

    return nums

def processLen5(input, nums):
    for o in filter( lambda l: len(l) == 5, input):
        if hasMatch(o,nums[1]):
            nums[3] = o
        elif hasMatch(o,extractPart( nums[4], nums[1])):
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
    return list(map( lambda l: ''.join(sorted(l)), input ))

result = 0
for line in open('input1.txt', 'r').readlines():
    (left,right) = splitInput( line )
    
    ov = prepareData( left )
    
    nums = processSimplest( ov )
    nums = processLen5( ov, nums )
    nums = processLen6( ov, nums )

    maps = nums2map(nums)
    result = result + code2int( right, maps )

print( result )