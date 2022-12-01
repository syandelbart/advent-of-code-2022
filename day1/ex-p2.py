current_calories = 0
calories = []

for line in open("./day1/input","r"):
  if line == "\n":
    calories.append(current_calories)
    current_calories = 0
    continue
  current_calories += int(line)

calories.sort(reverse=True)
print(sum(calories[0:3]))
