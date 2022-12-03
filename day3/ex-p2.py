common_priorities_all = []
elves_group_lines = []

def get_common_components_string(bag1,bag2):
    bag1_list = list(bag1)
    bag2_list = list(bag2)

    common_components = ""
    for i in range(len(bag1_list)):
        for j in range(len(bag2_list)):
            if bag1_list[i] == bag2_list[j]:
                common = bag1_list[i]
                if not common in common_components:
                    common_components += bag1_list[i]
    return common_components

for line in open("./day3/input","r"):
    elves_group_lines.append(line.strip())

    if len(elves_group_lines) != 3:
        continue

    elf1 = elves_group_lines[0]
    elf2 = elves_group_lines[1]
    elf3 = elves_group_lines[2]

    common_components = get_common_components_string(elf3,get_common_components_string(elf1,elf2))

    # calculate priorities
    common_priorities = []
    for component in common_components:
        if component.isupper():
            common_priorities.append(ord(component) - 38)
        else:
            common_priorities.append(ord(component) - 96)
    common_priorities_all.append(sum(common_priorities))

    elves_group_lines = []

print(sum(common_priorities_all))