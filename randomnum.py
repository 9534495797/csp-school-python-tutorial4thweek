import random
while True:
 user=int(input("your choice(1,2,3,4,5,6): "))
 num=[1,2,3,4,5,6]
 machine=random.choice(num)

 if user==machine:
        print("same choice so tied")
 elif user<machine:
        print("machine won b/c choice greater")
 else:
        print("user won b/c choice greater")
 next=input("continue(y/n): ")
 if next=="y":
    continue
 else:
    break
    
 

