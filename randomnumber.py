import random

user_input=input("Enter a choice:")
action=["rock","paper","scissors"]
machine_action=random.choice(action)
if user_input==machine_action:
    print("game is cancelled")
elif user_input=="rock":
    if machine_action=="scissors":
        print("user is the winner")
elif user_input=="paper":
    if machine_action=="scissors":
        print("machine is winner")
    else:
        print("user wins")
elif user_input=="rock":
    if machine_action=="paper":
        print("user is winner")
    else:
        print("machine is winner")
