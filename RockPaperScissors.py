import random

print("Welcome to Rock Paper Scissors!")

l1 = ["rock", "paper", "scissors"]

while 1 == 1:
    print("\n-------------------------------------------")
    player = input("Rock, Paper or Scissors?: ")
    r1 = random.choice(l1)

    if player == "rock" and r1 == "rock":
        print("\nYou chose" +player)
        print("Computer chose " +r1)
        print("Draw!")

    elif player == "rock" and r1 == "paper":
        print("You chose " +player)
        print("Computer chose" +r1)
        print("Computer wins!")

    elif player == "rock" and r1 == "scissors":
        print("You chose {player},")
        print("Computer chose {r1},")
        print("Player wins!")

    elif player == "paper" and r1 == "rock":
        print("You chose {player},")
        print("Computer chose {r1},")
        print("Player wins!")

    elif player == "paper" and r1 == "paper":
        print("You chose {player},")
        print("Computer chose {r1},")
        print("Draw!")

    elif player == "paper" and r1 == "scissors":
        print("You chose {player},")
        print("Computer chose {r1},")
        print("Computer wins!")

    elif player == "scissors" and r1 == "rock":
        print("You chose {player},")
        print("Computer chose {r1},")
        print("Computer wins!")

    elif player == "scissors" and r1 == "paper":
        print("You chose {player},")
        print("Computer chose {r1},")
        print("Player wins!")

    elif player == "scissors" and r1 == "scissors":
        print("You chose {player},")
        print("Computer chose {r1},")
        print("Draw!")

    else:
        print("Invalid Input!")