import re

cargo_list = []
rev = False
for line in open("./day5/input","r"):
    line_formatted = line.strip()
    line_chunks = list(line)


    if(not re.match("^move",line_formatted)):
        letter_index = 0
        for letter in range(1,len(line_chunks),4):
            cursor = line_chunks[letter]

            if len(cargo_list) < letter_index + 1:
                cargo_list.append([])

            if(cursor != ' ' and not re.match("[0-9]",cursor)):
                cargo_list[letter_index].append(cursor)

            letter_index += 1
    else:
        if not rev:
            for stack in cargo_list:
                stack.reverse()
            rev = True


        if line != '':
            move_split = re.findall("\d{1,2}",line_formatted)
            move_amount,origin,destination = map(int,move_split)

            for move_cursor in range(0,move_amount):
                cargo_list[destination - 1].append(cargo_list[origin - 1].pop())
                    





print("The code is: ",end="")
for stack in cargo_list:
    print(stack[-1],end="")
print()