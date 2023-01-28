import random



user_input=input("your choice (rock,paper,scissors): ")
input=["rock","paper","scissors"]
machine_input=random.choice(input)
print(f"machine choose{machine_input} and user choose{user_input}")

if user_input==machine_input:

    print("both choose same so tie")
elif user_input=="scissors":
     if machine_input=="paper":
        print("user won")
     else:
        print("machine won")
elif user_input=="paper":
     if machine_input=="rock":
        print("user won")
     else:
        print("machie won")
elif user_input=="rock":
     if machine_input=="scissors":
        print("user won")
     else:
        print("machine won")



# import random
# while True:
#     user_input=input("your choice (rock,paper,scissors): ")
#     input=["rock","paper","scissors"]
#     machine_input=random.choice(input)

#     if user_input==machine_input:

#      print("both choose same so tie")
# elif user_input=="rock":
#      if machine_input=="paper":
#         print("machine won")
#      else:
#         print("user won")
# elif user_input=="paper":
#      if machine_input=="scissors":
#         print("machine won")
#      else:
#         print("user won")
# elif user_input=="scissors":
#      if machine_input=="rock":
#         print("machine won")
#      else:
#         print("user won")





