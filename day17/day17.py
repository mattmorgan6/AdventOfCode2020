import collections


SIZE = 21

def part_2_code(arr):

    # 80 W,Z,Y,X directions
    dirs = [(-1,0,1,-1), (-1,0,1,0), (-1,0,1,1), (-1,0,0,1), (-1,0,-1,1), (-1,0,-1,0), (-1,0,-1,-1), (-1,0,0,-1),  
            (-1,1,1,-1), (-1,1,1,0), (-1,1,1,1), (-1,1,0,1), (-1,1,-1,1), (-1,1,-1,0), (-1,1,-1,-1), (-1,1,0,-1),  
            (-1,-1,1,-1), (-1,-1,1,0), (-1,-1,1,1), (-1,-1,0,1), (-1,-1,-1,1), (-1,-1,-1,0), (-1,-1,-1,-1), (-1,-1,0,-1),
            (-1,1,0,0), (-1,-1,0,0),
            (0,0,1,-1), (0,0,1,0), (0,0,1,1), (0,0,0,1), (0,0,-1,1), (0,0,-1,0), (0,0,-1,-1), (0,0,0,-1),  
            (0,1,1,-1), (0,1,1,0), (0,1,1,1), (0,1,0,1), (0,1,-1,1), (0,1,-1,0), (0,1,-1,-1), (0,1,0,-1),  
            (0,-1,1,-1), (0,-1,1,0), (0,-1,1,1), (0,-1,0,1), (0,-1,-1,1), (0,-1,-1,0), (0,-1,-1,-1), (0,-1,0,-1),
            (0,1,0,0), (0,-1,0,0),
            (1,0,1,-1), (1,0,1,0), (1,0,1,1), (1,0,0,1), (1,0,-1,1), (1,0,-1,0), (1,0,-1,-1), (1,0,0,-1),  
            (1,1,1,-1), (1,1,1,0), (1,1,1,1), (1,1,0,1), (1,1,-1,1), (1,1,-1,0), (1,1,-1,-1), (1,1,0,-1),  
            (1,-1,1,-1), (1,-1,1,0), (1,-1,1,1), (1,-1,0,1), (1,-1,-1,1), (1,-1,-1,0), (1,-1,-1,-1), (1,-1,0,-1),
            (1,1,0,0), (1,-1,0,0),
            (1,0,0,0),(-1,0,0,0)]



    copy = [[[[0 for k in range(SIZE)] for i in range(SIZE)] for j in range(SIZE)] for l in range(SIZE)]    

    for w in range(SIZE):
        for z in range(SIZE):
            for y in range(SIZE):
                for x in range(SIZE):

                    neighbors_alive = 0

                    killed = 0
                    if arr[w][z][y][x] == 1:
                        # ACTIVE
                        for d_w, d_z, d_y, d_x in dirs:
                            n_w, n_z, n_y, n_x = w + d_w, z + d_z, y + d_y, x + d_x
                            if n_w < 0 or n_w >= SIZE or n_z < 0 or n_z >= SIZE or n_y < 0 or n_y >= SIZE or n_x < 0 or n_x >= SIZE:
                                continue

                            if arr[n_w][n_z][n_y][n_x] == 1:
                                neighbors_alive += 1

                        if neighbors_alive == 2 or neighbors_alive == 3:
                            copy[w][z][y][x] = 1
                        else:
                            copy[w][z][y][x] = 0
                            killed += 1

                    else:
                        # INACTIVE
                        
                        # check neighbors to calculate current value
                        for d_w, d_z, d_y, d_x in dirs:
                            n_w, n_z, n_y, n_x = w + d_w, z + d_z, y + d_y, x + d_x
                            if n_w < 0 or n_w >= SIZE or n_z < 0 or n_z >= SIZE or n_y < 0 or n_y >= SIZE or n_x < 0 or n_x >= SIZE:
                                continue

                            if arr[n_w][n_z][n_y][n_x] == 1:
                                neighbors_alive += 1

                        if neighbors_alive == 3:
                            copy[w][z][y][x] = 1

    arr = copy

    return arr






arr = [[[[0 for k in range(SIZE)] for i in range(SIZE)] for j in range(SIZE)] for l in range(SIZE)]   # 5,5,5,5 is the middle



input_file_path = "input2.in"
# input_file_path = "input2.in"
with open(input_file_path) as infile:

    k = 8
    for i in range(k):
        next = infile.readline().strip()
        for j in range(k):
            if next[j] == '#':
                arr[10][10][10 + i-(k//2)][10 + j-(k//2)] = 1    # starts with 29, 29, 0 for z, y, x

for x in range(6):
    arr = part_2_code(arr)
    print(x)

sum = 0
for w in range(SIZE):
    for z in range(SIZE):
        for y in range(SIZE):
            for x in range(SIZE):
                if arr[w][z][y][x] == 1:
                    sum += 1
print(sum)















# ans2 = part_2_code()
# print(ans2)




def test():
    pass





# def part_1_code(arr[w]):

#     # 26 Z,Y,X directions
#     dirs = [(0,1,-1), (0,1,0), (0,1,1), (0,0,1), (0,-1,1), (0,-1,0), (0,-1,-1), (0,0,-1),  
#             (1,1,-1), (1,1,0), (1,1,1), (1,0,1), (1,-1,1), (1,-1,0), (1,-1,-1), (1,0,-1),  
#             (-1,1,-1), (-1,1,0), (-1,1,1), (-1,0,1), (-1,-1,1), (-1,-1,0), (-1,-1,-1), (-1,0,-1),
#             (1,0,0), (-1,0,0)]


#     copy = [[[0 for k in range(SIZE)] for i in range(SIZE)] for j in range(SIZE)]    # 5,5,5 is the middle

#     for z in range(SIZE):
#         for y in range(SIZE):
#             for x in range(SIZE):

#                 neighbors_alive = 0

#                 killed = 0
#                 if arr[w][z][y][x] == 1:
#                     # ACTIVE
#                     for d_z, d_y, d_x in dirs:
#                         n_z, n_y, n_x = z + d_z, y + d_y, x + d_x
#                         if n_z < 0 or n_z >= SIZE or n_y < 0 or n_y >= SIZE or n_x < 0 or n_x >= SIZE:
#                             continue

#                         if arr[w][n_z][n_y][n_x] == 1:
#                             neighbors_alive += 1

#                     if neighbors_alive == 2 or neighbors_alive == 3:
#                         copy[w][z][y][x] = 1
#                     else:
#                         copy[w][z][y][x] = 0
#                         killed += 1

#                 else:
#                     # INACTIVE
                    
#                     # check neighbors to calculate current value
#                     for d_z, d_y, d_x in dirs:
#                         n_z, n_y, n_x = z + d_z, y + d_y, x + d_x
#                         if n_z < 0 or n_z >= SIZE or n_y < 0 or n_y >= SIZE or n_x < 0 or n_x >= SIZE:
#                             continue

#                         if arr[w][n_z][n_y][n_x] == 1:
#                             neighbors_alive += 1

#                     if neighbors_alive == 3:
#                         copy[w][z][y][x] = 1

#     arr[w] = copy

#     # print(killed)
#     return arr[w]

