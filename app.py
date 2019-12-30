import random

print("""THAT'S ROCK PAPER SCISSORS GAME
You will play with the computer
Type R-for rock
Type P-for paper
Type S-for scissors
Who win two rounds win
Good luck

""")

i = 1
p_score = 0
c_score = 0

while p_score < 2 and c_score < 2:
    print(f"""
{i} round:               com {c_score}: plr {p_score}""")
    computer = random.choice(["R", "P", "S"])
    print(computer)
    player = (input("Your choice: "))
    if player == "R":
        if computer == "R":
            print("Draw, no points")
        if computer == "P":
            print("You lose")
            c_score += 1
        if computer == "S":
            print("You win")
            p_score += 1
    elif player == "P":
        if computer == "R":
            print("You win")
            p_score += 1
        if computer == "P":
            print("Draw, no points")
        if computer == "S":
            print("You lose")
            c_score += 1
    elif player == "S":
        if computer == "R":
            print("You lose")
            c_score += 1
        if computer == "P":
            print("You win")
            p_score += 1
        if computer == "S":
            print("Draw, no points")
    i += 1


if c_score == 2:
    print("Sorry, but you have lost the game")

elif p_score == 2:
    print("Congrats, you have just won the game")