import random

items_list=["Rock","Paper","Scissor"]
user_choice = input("Enter the move: Rock, Paper, Scissor: ").capitalize()
comp_choice = random.choice(items_list)

print(f"You chose = {user_choice}, Computer chose = {comp_choice}")


if user_choice not in items_list:
    print("Invalid move! Please choose Rock, Paper, or Scissor.")
elif user_choice == comp_choice:
    print("Match tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock, Computer Win!!")
    else:
        print("Rock smashes Scissor, You Win!!")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts Paper, Computer Win!!")
    else:
        print("Paper covers Rock, You Win!!")
        
elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts Paper, You Win!!")
    else:
        print("Rock smashes Scissor, Computer Win!!")