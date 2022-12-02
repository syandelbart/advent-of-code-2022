symbols = {
  "A": "rock",
  "B": "paper",
  "C": "scissors",
  "X": "lose",
  "Y": "draw",
  "Z": "win"
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
  player1, end = line.strip().split(" ")

  outcome_wanted = symbols[end]

  score = outcomes[outcome_wanted]
  score += bonus[symbols[player1]] if outcome_wanted == "draw" else bonus[effects[outcome_wanted][symbols[player1]]]

  scores.append(score)

print(sum(scores))