pair_amount = 0

for line in open("./day4/input","r"):
    sections_split = line.strip().split(",")
    elf1_start,elf1_end = list(map(int,sections_split[0].split("-")))
    elf2_start,elf2_end = list(map(int,sections_split[1].split("-")))

    if len(set(range(elf1_start,elf1_end + 1)).intersection(set(range(elf2_start,elf2_end + 1)))) > 0:
        pair_amount += 1


print(pair_amount)

