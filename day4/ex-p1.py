pair_amount = 0

for line in open("./day4/input","r"):
    sections_split = line.strip().split(",")
    print(sections_split)
    elf1_start,elf1_end = list(map(int,sections_split[0].split("-")))
    elf2_start,elf2_end = list(map(int,sections_split[1].split("-")))

    if ((elf1_start - elf2_start <= 0) and (elf2_end - elf1_end <= 0)) or (elf2_start - elf1_start <= 0) and (elf1_end - elf2_end <= 0):
        pair_amount += 1

print(pair_amount)

