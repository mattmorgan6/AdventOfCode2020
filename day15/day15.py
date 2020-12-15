import collections

def part_2_code(start_arr):
    dict = {}

    for i in range(len(start_arr)):
        num = start_arr[i]
        dict[num]= (-1, i+1)

    i = len(start_arr)

    last = 0
    while i < 30000000:
        i += 1                  
        if last not in dict:
            last = 0
            dict[last] = (-1, i)
        else:
            indices = dict[last]
            if indices[0] == -1:
                last = 0
                dict[last] = (dict[last][1], i)
            else:
                diff = indices[1] - indices[0]
                last = diff
                if last in dict:
                    first, second = dict[last]
                    dict[last] = (second, i)
                else:
                    dict[last] = (-1, i)

        # print(last, end=' ')

    return last


ans = part_2_code([6,4,12,1,20,0,16])
print(ans)






def part_1_code(start_arr):
    dict = {}

    for i in range(len(start_arr)):
        num = start_arr[i]
        dict[num] = [i+1]
              
    i = len(start_arr)

    last = 0
    while i < 2020:
        i += 1                  
        if last not in dict:
            last = 0
            dict[last] = [i]
        else:
            indices = dict[last]
            if len(indices) == 1:
                last = 0
                dict[last].append(i)
            else:
                diff = indices[-1] - indices[2]
                last = diff
                if last in dict:
                    dict[last].append(i)
                else:
                    dict[last] = [i]

        # print(last)


    return last
