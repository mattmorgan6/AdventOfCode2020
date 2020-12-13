
def code(A):
    ready = set()
    used = set()
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            used.add((A[i], A[j]))

    for num in A:
        for tup in used:
            if num != tup[0] and num != tup[1]:
                s = tup[0] + tup[1]
                comp = 2020 - s
                if num == comp:
                    return num * tup[0] * tup[1]

    return -1
    





A = []
input_file_path = "day1.in"
with open(input_file_path) as infile:
    t = True
    while t:
        num = infile.readline().strip()
        if num != '':
            A.append(int(num))
        else:
            break


ans = code(A)

print(ans)
