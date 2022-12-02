symbols = {
  "A": "rock",
  "B": "paper",
  "C": "scissors",
  "X": "rock",
  "Y": "paper",
  "Z": "scissors"
}

bonus = {
  "rock": 1,
  "paper": 2,
  "scissors": 3
}

effects = {
  "win" : {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
  },
  "lose" : {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
  }
}

outcomes = {
  "win": 6,
  "draw": 3,
  "lose": 0
}

scores = []
for line in open("./day2/input","r"):
  player1,player2 = line.strip().split(" ")


  if symbols[player1] == symbols[player2]:
    score = outcomes["draw"]
  else:
    score = outcomes["win"] if effects["win"][symbols[player1]] is symbols[player2] else outcomes["lose"]

  score += bonus[symbols[player2]]

  scores.append(score)

print(sum(scores))