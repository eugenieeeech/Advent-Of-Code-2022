from enum import Enum

# read input textfile from same path
scores = 0
winning_score = 0
task2 = 0


class PlayerChoice(Enum):
    X = 1  # Rock if opponent is C then player win
    Y = 2  # Paper if opponent is A then player win
    Z = 3  # Scissors if opponent is B then player win


class OpponentChoice(Enum):
    A = 1
    B = 2
    C = 3


# For Task 2
def win(col):
    if col == 'A':
        return 2
    elif col == 'B':
        return 3
    elif col == 'C':
        return 1


def lose(col):
    if col == 'A':
        return 3
    elif col == 'B':
        return 1
    elif col == 'C':
        return 2


with open("input.txt") as f:
    for line in f.readlines():
        if (line != "") & (line != "\n"):
            inputLine = list(line)
            opponent = inputLine[0]
            player = inputLine[2]
            if (player == 'X' and opponent == 'C') or (player == 'Y' and opponent == 'A') or (
                    player == 'Z' and opponent == 'B'):
                winning_score = 6
            elif OpponentChoice[opponent].value == PlayerChoice[player].value:
                winning_score = 3
            else:
                winning_score = 0
            scores = scores + PlayerChoice[player].value + winning_score
            # Task 2
            if player == 'Z':
                task2 = task2 + win(opponent) + 6
            elif player == 'Y':
                task2 = task2 + OpponentChoice[opponent].value + 3
            else:  # lose
                task2 = task2 + lose(opponent) + 0

# Task 1
print(scores)
# Task 2
print(task2)
