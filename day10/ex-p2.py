

cycle = 0
crt_line = ""
total = 1
real_total = 0
doStop = False
cyclesCompleted = True
for (index,line) in enumerate(open("./day10/input","r")):
    line_chunks = line.strip().split(" ")

    instruction = line_chunks[0]
    value = int(line_chunks[1] if len(line_chunks) > 1 else 0)


    if(instruction == "noop"):
        required_cycles = 1
    elif(instruction == "addx"):
        required_cycles = 2
        
    for x in range(0,required_cycles):
        cycle += 1

        if abs((cycle - 1) % 40 - total) <= 1:
            crt_line += "#"
        else:
            crt_line += "."
        if cycle % 40 == 0:
            crt_line += "\n"
        if cycle == 20 or (cycle - 20) % 40 == 0:
            real_total += total * cycle


    if doStop:
        break

    if(instruction == "addx"):
        total += value


print("CRT Output\n",crt_line)