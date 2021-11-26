from random import choice

size_ship = [3,2,1,0]

ship_catalog = [1,2,3,4]

Battleship = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(2,1),(3,1),(4,1),(4,0),(4,-1),(3,-1),(2,-1),(1,-1),(0,-1)]
Carrier = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(2,1),(3,1),(3,0),(3,-1),(2,-1),(1,-1),(0,-1)]
Cruiser = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(2,1),(2,0),(2,-1),(1,-1),(0,-1)]
Destroyer = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]

battlefield = [[0] * 12 for i in range(12)]
for n in ship_catalog:
    for m in range(n):
        flag_angle = choice([0,1])
        A = []
        m,k = 11,11 - size_ship[n-1]
        if (flag_angle == 1): m,k = k,m
        
        for i in range(1,m):
            for j in range(1,k):
                if ((flag_angle ==0 and battlefield[i][j] == 0 and battlefield[i][j + size_ship[n-1]] == 0) or (flag_angle == 1 and battlefield[i][j] == 0 and battlefield[i + size_ship[n-1]][j] == 0)):
                        A.append((i,j))
                        
        coord = choice(A)
        
        for i in range(0,size_ship[n-1] + 1):
            if (flag_angle == 0):
                battlefield[coord[0]][coord[1] + i] = size_ship[n-1] + 2
            else:
                battlefield[coord[0]+i][coord[1]] = size_ship[n-1] + 2

        if (n == 1) : B = Battleship
        elif (n == 2) : B = Carrier
        elif (n == 3) : B = Cruiser
        else: B = Destroyer
        
        for i in range(len(B)):
            if (flag_angle == 0):
                battlefield[int(coord[0] + B[i][1])][int(coord[1] + B[i][0])] = 1
            else:
                battlefield[int(coord[0] + B[i][0])][int(coord[1] + B[i][1])] = 1


print(' ')
for row in battlefield:
    print(' '.join([str(elem) for elem in row]))
