import random
while True:
    user_action = input("Enter a choice (rock,paper,scissors): ")
    possible_action = ["Rock", "Paper", "Scissors", "rock", "paper", "scissors"]
    computer_action = random.choice(possible_action)
    print(user_action)
    print(computer_action)

    if user_action == computer_action:
        print(f"You chose {user_action} and the computer chose {computer_action}")
        print("Its a TIE")
    elif user_action == "rock":
        if computer_action == "Scissors":
            print("YOU WIN!!!")
        else:
            print("YOU LOSE!!!")
    elif user_action == "Paper":
        if computer_action == "Rock":
            print("YOU WIN!!!")
        else:
            print("You loose")
    elif user_action == "Scissors":
        if computer_action == "Papers":
            print("YOU WIN!!!")
        else:
            print("You Loose")
    else:
        print("choose correct choice")
    play_again = input("Play again? (y/n):")
    if play_again.lower() != "y":
        break



