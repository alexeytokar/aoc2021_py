import re
input = open('test1.txt', 'r')
line = input.readline()
inums = list(map(int, line.strip().split(",")))

boards_num = 100
boards = [None]*boards_num # [ { sum :, rows: [ numcrossed ], cols: [ numcrossed ], nums:[] } ]
nums = {} # { 'num' : [ (boardid, colid, rowid) ] }

board_idx = -1
while line:
    line = input.readline()
    if not line.strip():
        board_idx += 1
        col_idx = 0
        row_idx = 0
        if board_idx < boards_num:
            boards[board_idx] = { "rows" : [0]*5, "cols": [0]*5, "nums" : []*25 }
    else:
        
        rnums = list(map(int, re.split(" +",line.strip())))
        for n in rnums:
            boards[board_idx]['nums'].append( n )
            if n not in nums:
                nums[n] = []
            nums[n].append( (board_idx, col_idx, row_idx) )
            col_idx += 1
        row_idx += 1 
        col_idx = 0

curr_sum = 0
for n in inums:
    curr_sum += n
    
    all = nums[n]
    for a in all:
        (boardid, colid, rowid) = a
        boards[boardid]['nums'].remove(n)
        boards[boardid]['rows'][rowid] += 1
        boards[boardid]['cols'][colid] += 1
        if boards[boardid]['rows'][rowid] == 5 or boards[boardid]['cols'][colid] == 5:
            print( sum(boards[boardid]['nums'])*n )
            
            exit()

    
