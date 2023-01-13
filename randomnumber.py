import random
while True:
    user_input=input("your choice(rock,paper,scissors):")
    random_num=["rock","paper","scissors"]
    computer_input=random.choice(random_num)
    print(f"you choose {user_input}, computr choose {computer_input}")

    if user_input==computer_input:
        print("match tie")
    elif user_input=="rock":
        if computer_input=="paper":
            print("paper catch rock u win!")
        else:
            print("computer wins")
    elif user_input=="paper":
        if computer_input=="scissors":
            print("computer wins")
        else:
            print("user wins")   
    elif user_input=="scissors":
        if computer_input=="rock":
            print("computer wins") 
        else:
            print("user wins")
    play_again=input(("y or n: " ))
    if play_again=="y":
        continue
    else:
        break    