import random 

cscore = 0
hscore = 0

while True:
    
    print(f"computer score: {cscore} \t your score: {hscore}\n")

    user_choice = int(input("1 for stone, 2 for paper, 3 for scissor choose: "))
    computer_choice = random.randint(1, 3)
    
    if user_choice == 1 and computer_choice == 3:
        hscore += 1
        print("you won the round\n")
    elif user_choice == 2 and computer_choice == 1:
        hscore += 1
        print("you won the round\n")
    elif user_choice == 3 and computer_choice == 2:
        hscore += 1
        print("you won the round\n")
    elif user_choice == computer_choice:
        print("its a tie\n")
    else:
        cscore += 1
        print("you lost the round\n")

    if cscore == 5:
        print("computer won the game")
        break
    elif hscore == 5:
        print("you won the game")
        break