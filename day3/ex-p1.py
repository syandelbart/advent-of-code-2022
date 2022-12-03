common_priorities_all = []

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
    compartment1 = line[0:int(len(line)/2)]
    compartment2 = line[int(len(line)/2):]

    common_components = get_common_components_string(compartment1,compartment2)

    # calculate priorities
    common_priorities = []
    for component in common_components:
        if component.isupper():
            common_priorities.append(ord(component) - 38)
        else:
            common_priorities.append(ord(component) - 96)
    common_priorities_all.append(sum(common_priorities))

print(sum(common_priorities_all))