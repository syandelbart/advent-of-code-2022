max_calories = 0
current_calories = 0

for line in open("./day1/input","r"):
  if line is "\n":
    if(current_calories > max_calories):
      max_calories = current_calories
    current_calories = 0
    continue
  current_calories += int(line)

print(max_calories)
