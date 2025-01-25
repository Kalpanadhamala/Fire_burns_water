import random

def fire_grass_burns():
    options = ["fire","grass","burns"]
    user_score = 0
    computer_score = 0
    name = (input("Enter your name = "))
    print(f"Hello {name}, Thanks for choosing us. ")

    rounds = int(input(f"\nEnter the round no. you want to play = "))
    for i in range(1,rounds+1):
        print(f"\nRound:{i}")
        print("Choose Options:'fire','grass','burns'")
        user_choice = input("Enter your choice: ").strip().lower()
        
        if user_choice not in options:
            print("Invalid choice! Please choice fire,grass,burns")
            continue
        
        computer_choice = random.choice(options)
        print("Computer choice: ", computer_choice)
        
        if user_choice == computer_choice:
            print("it is draw")
        elif(user_choice == "fire" and computer_choice == "grass") or \
            (user_choice == "grass" and computer_choice == "burns") or \
            (user_choice == "burns" and computer_choice == "fire"):
            print(f"{name} won the game. ")
            user_score += 1
        else:
            print("Computer won the game.")
            computer_score += 1

    print("\n....Game Over.....")
    print(f"{name}'s Score: {user_score}")
    print(f"Computer's Score: {computer_score}")


    if user_score > computer_score:
        print(f"Overall , {name} won the game. Congratulation!")
    elif computer_score > user_score:
        print("Overall, Computer won the game. Congratulation!")
    else:
        print("Its tie")
    print("Thank you!")
    
fire_grass_burns()