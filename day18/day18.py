import collections


def part_1_code(data):

    stack = []

    index = 0

    # PARAM: ending is the number of parenthesis left on the left.
    def do_stuff(ending):
        if len(stack) <= 2:
            return

        is_num, i = stack[-1]
        
        if is_num == True:
            a = stack[-3]
            if stack[-3][0] == True:
                operator = stack[-2][1]
                new_num = 0
                if operator == '+':
                    new_num = stack[-3][1] + i
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    stack.append((True, new_num))
                elif operator == '*':
                    # DON'T DO UNTIL PARENTHESIS LEFT OR END
                    if ending >= 1:
                        new_num = stack[-3][1] * i
                        stack.pop()
                        stack.pop()
                        stack.pop()
                        stack.append((True, new_num))
        else:
            if i == ')':
                stack.pop()
                ending += 1
                
        # If there are parethesis left on the left:                
        if ending > 0:
            if len(stack) == 1:
                return stack[-1]
                
            if stack[-2][1] == '(':
                del stack[-2]
                ending -= 1
            do_stuff(ending)

        # If we reached the end and need to do some more multiplication
        if index == len(data) - 1 and len(stack) > 1:
            if stack[-2][1] == '(':
                del stack[-2]
                ending -= 1
            do_stuff(ending + 1)
       

    while index < len(data):
        i = data[index]
        if ord(i) <= ord('9') and ord(i) >= ord('0'):
            # number
            i = int(i)
            stack.append((True, i))

        else:
            # operator
            stack.append((False, i))

        do_stuff(0)
        index += 1

    return stack[-1]


# Warning: you have to modify the input file so that every character including '(' and ')' are surrounded by spaces

# input_file_path = "input1.in"
input_file_path = "input2.in"
sum = 0
with open(input_file_path) as infile:
    while True:
        stack = []
        next = infile.readline().strip()
        if next != '':
            data = next.split()
            ans = part_1_code(data)
            sum += ans[1]
        else:
            break


print(sum)
