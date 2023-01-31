import random
while True:
    user_input=input("your choice (rock,paper,scissors): ")
    value=["rock","paper","scissors"]
    machine_input=random.choice(value)
    print(f"u choose {user_input} and machine choose {machine_input}")

    if user_input==machine_input:
        print("match tie!")
    elif user_input=="rock":
        if machine_input=="paper":
            print("macchine won")
        else:
            print("user won")
    elif user_input=="paper":
        if machine_input=="scissors":
            print("machine won")
        else:
            print("uswr won")
    elif user_input=="scissors":
        if machine_input=="rock":
            print("machine won")
        else:
            print("user won")
    x=input("want to continue(y/n):")
    if x=="n":
        break