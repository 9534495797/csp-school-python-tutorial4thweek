n = int(input("your num: "))
fact = 1

for i in range(1,n+1):
  fact = fact * i

print (f"The factorial of {n} is : ",end="")
print (fact)