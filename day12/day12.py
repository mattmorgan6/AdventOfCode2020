
# Params: list of tuples in format (direction, distance)
def code(arr):
    s_x = 0
    s_y = 0
    w_x = 10  # relative to the ship
    w_y = 1  # relative to the ship
    heading = 0  # initially east    0,1,2,3 = E,S,W,N

    for instruction in arr:
        if instruction[0] == 'R':
            for i in range(instruction[1] // 90):
                w_x, w_y = w_y, w_x
                w_y *= -1
    
        if instruction[0] == 'L':
            for i in range(instruction[1] // 90):
                w_x, w_y = w_y, w_x
                w_x *= -1

        elif instruction[0] == 'F':
            s_x += w_x * instruction[1]
            s_y += w_y * instruction[1]
        elif instruction[0] == 'E':
            w_x += instruction[1]
        elif instruction[0] == 'W':
            w_x -= instruction[1]
        elif instruction[0] == 'N':
            w_y += instruction[1]
        elif instruction[0] == 'S':
            w_y -= instruction[1]

    return abs(s_x) + abs(s_y)


arr = []
input_file_path = "day12.in"
with open(input_file_path) as infile:
    t = True
    while t:
        ins = infile.readline().strip()
        if ins != '':
            kind = ins[0]
            dist = int(ins[1:])
            arr.append((kind, dist))
        else:
            break


ans = code(arr)

print(ans)




# Params: list of tuples in format (direction, distance)
def part_1_code(arr):
    x = 0
    y = 0
    heading = 0  # initially east    0,1,2,3 = E,S,W,N

    for instruction in arr:
        if instruction[0] == 'R':
            d = instruction[1] // 90
            for i in range(d):
                if heading == 3:
                    heading = 0
                else:
                    heading += 1
        if instruction[0] == 'L':
            d = instruction[1]
            d = instruction[1] // 90
            for i in range(d):
                if heading == 0:
                    heading = 3
                else:
                    heading -= 1

        elif instruction[0] == 'F':
            if heading == 0:    # East
                x += instruction[1]
            elif heading == 2:  # West
                x -= instruction[1]
            elif heading == 3:  # North
                y += instruction[1]
            elif heading == 1:  # South
                y -= instruction[1]
        elif instruction[0] == 'E':
            x += instruction[1]
        elif instruction[0] == 'W':
            x -= instruction[1]
        elif instruction[0] == 'N':
            y += instruction[1]
        elif instruction[0] == 'S':
            y -= instruction[1]

    return abs(x) + abs(y)