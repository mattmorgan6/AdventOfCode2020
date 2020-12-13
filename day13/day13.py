
# Params: list of tuples in format (id, index)
def part_2_code(arr):
    i = 0
    p_k = 0 # keeps track of our record for buses in a row, this is useful for our loop
    skip = 1
    while i < 100000000000000:
        # r1 is the timestamp the first bus arrives
        r1 = arr[0][0] * i

        # Loop through each bus id in the array
        for k in range(1, len(arr)):
            num = arr[k][0]
            index = arr[k][1]

            # check if the bus id arrives at time we want
            if (r1 + index) % num == 0:

                # if it is a new bus id that has arrived on time before, but does for this time,
                # update the skip so that we can iterate through the array much faster
                # by skipping times we know will not work.
                if k > p_k:
                    # if o
                    p_k = k
                    skip = skip * arr[k][0]

                # if the final bus id works then return our answer
                if k == len(arr) - 1:
                    return r1

            else:
                # Restart the next timestamp because one of our buses arrrive at the time we wanted
                break

        i += skip

    return -1


arr = []
input_file_path = "day13.in"
with open(input_file_path) as infile:
    num = int(infile.readline().strip())
    ids = infile.readline().split(',')
    for i in range(len(ids)):
        id = ids[i]
        if id != 'x':
            arr.append((int(id), i))
    
ans = part_2_code(arr)

print(ans)


























# Params: list of tuples in format (direction, distance)
def part_1_code(arr):
    routes = []

    # go through each bus id in arr
    for x in arr:
        remainder = x - num % x
        routes.append((remainder,x))
    
    routes.sort()

    return routes[0][0] * routes[0][1]

