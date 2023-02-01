import random
while True:
    user_input=int(input("your choice(1,2,3,4,5,6): "))
    value=[1,2,3,4,5,6]
    machine_input=random.choice(value)
    print(f"you choose {user_input} computer choose{machine_input}")

    if user_input==machine_input:
        print("mach tied!")
    elif user_input<machine_input:
        print(f"user loose b/c{machine_input} is larger than {user_input}")
    else:
        print(f"user won b/c {user_input} is larger than {machine_input}")
    
    x=input("want to continue(y/n)")
    if x=="n":
        break
    

