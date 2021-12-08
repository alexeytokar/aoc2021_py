input = open('input1.txt', 'r')
lines = input.readlines()
cnt = 0;
for line in lines:
    p = line.strip().split(" | ")
    os = p[1].split( " " )
    for o in os:
        if len(o) == 7 or len(o) <= 4:
            cnt = cnt + 1


print( cnt )