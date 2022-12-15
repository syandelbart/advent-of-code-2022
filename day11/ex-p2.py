import yaml
from typing import Self
from enum import Enum
import math

class Operator(Enum):
    MULTIPLY = 1
    DIVIDE = 1
    ADD = 3
    SUBTRACT = 4

def get_operator_enum_from_string(operator : str) -> Operator:
    if(operator == "*"):
        return Operator.MULTIPLY
    elif(operator == "+"):
        return Operator.ADD
    else:
        return -1

def get_operator_enum_from_phrase(operator : str) -> Operator:
    if(operator == ""):
        return Operator.MULTIPLY
    elif(operator == "+"):
        return Operator.ADD
    else:
        return -1

class Monkey:
    starting_items : list
    worry_operator : Operator
    worry_factor : int
    test_operator : Operator
    test_factor : int
    monkey_throw_int_if_true : int
    monkey_throw_int_if_false : int
    monkey_throw_if_true : Self
    monkey_throw_if_false : Self
    times_inspected : int
    def __init__(self, starting_items : list, worry_operator : Operator, worry_factor : int, test_operator : Operator, test_factor : int, monkey_throw_int_if_true : int, monkey_throw_int_if_false : int):
        self.starting_items = starting_items or list()
        self.worry_operator = worry_operator or -1
        self.worry_factor = worry_factor or -1
        self.test_operator = test_operator or -1
        self.test_factor = test_factor or -1
        self.monkey_throw_int_if_true = monkey_throw_int_if_true
        self.monkey_throw_int_if_false = monkey_throw_int_if_false
        self.times_inspected = 0
    def increase_times_inspected(self):
        self.times_inspected += len(self.starting_items)
    def set_worry_level(self, index : int, worry_level : int):
        self.starting_items[index] = worry_level
        return worry_level
    def get_current_worry_level(self, index : int = 0):
        return self.starting_items[index]
    def get_calculated_worry_level(self, index : int = 0):
        worry_factor = self.worry_factor
        if(worry_factor == "old"):
            worry_factor = self.starting_items[index]
        worry_factor = int(worry_factor)
        if(self.worry_operator == Operator.MULTIPLY):
            return self.starting_items[index] * worry_factor
        elif(self.worry_operator == Operator.ADD):
            return self.starting_items[index] + worry_factor
    def get_test_factor(self):
        return self.test_factor
    def get_throw_true(self):
        return self.monkey_throw_int_if_true
    def get_throw_false(self):
        return self.monkey_throw_int_if_false
    def remove_item(self,index = 0):
        return self.starting_items.pop(index)
    def add_item(self,item : int,index : int = -1):
        if index == -1:
            index = len(self.starting_items)
        return self.starting_items.insert(index, item)

with open("./day11/input","r") as file:
    filedata = file.read()
monkey_information = yaml.safe_load(filedata.replace("    ","  "))

monkeys : list[Monkey] = list()

for monkey in monkey_information:
    monkey_values = monkey_information[monkey]
    starting_items = list(map(int,str(monkey_values["Starting items"]).split(",")))
    worry_operator = get_operator_enum_from_string(str(monkey_values["Operation"]).split(" ")[-2])
    worry_factor = str(monkey_values["Operation"]).split(" ")[-1]
    test_operator = Operator.DIVIDE
    test_factor = int(str(monkey_values["Test"]).split(" ")[-1])
    monkey_throw_int_if_true = int(str(monkey_values["If true"]).split(" ")[-1])
    monkey_throw_int_if_false = int(str(monkey_values["If false"]).split(" ")[-1])




    monkeys.append(Monkey(starting_items,worry_operator,worry_factor,test_operator,test_factor,monkey_throw_int_if_true,monkey_throw_int_if_false))



lcm = math.lcm(*[item for monkey in monkeys for item in monkey.starting_items])
print("Common denom:",lcm)

rounds = 10000
for round in range(0,rounds):
    for (monkey_index, monkey) in enumerate(monkeys):
        monkey.increase_times_inspected()
        # print("Monkey",monkey_index,":")
        index = 0
        while len(monkey.starting_items) > 0:
            item = monkey.starting_items[0]
            # print("\tMonkey inspects an item with a worry level of {worry_level}.".format(worry_level=monkey.get_current_worry_level(0)))
            new_worry_level = monkey.set_worry_level(0,int(monkey.get_calculated_worry_level(0) % lcm) )
            # print(" \t\tTo:",new_worry_level)
            if(new_worry_level % monkey.get_test_factor() == 0):
                monkeys[monkey.get_throw_true()].add_item(monkey.remove_item(0))
                # print("\t\tThrow to: ",monkey.get_throw_true())
            else:
                monkeys[monkey.get_throw_false()].add_item(monkey.remove_item(0))
                # print("\t\tThrow to: ",monkey.get_throw_false())
            index += 1

item_map : list[int] = list()
for monkey in monkeys:
    item_map.append(monkey.times_inspected)

item_map.sort(reverse=True)
print("Map:",item_map)
print("{item1} * {item2} =".format(item1=item_map[0],item2=item_map[1]),item_map[0] * item_map[1])