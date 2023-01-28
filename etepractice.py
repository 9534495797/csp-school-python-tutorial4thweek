# # def operations(a,b):
# #     return a+b, a-b,a*b,a/b,a%b
# # print(operations(2,4))

# # Python program to check if the number is an Armstrong number or not

# # take input from the user
# num = int(input("Enter a number: "))

# # initialize sum
# sum = 0

# # find the sum of the cube of each digit
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10

# # display the result
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")

num=int(input("your num: "))
sum=0
temp=num
while temp>0:
    digit = temp%10
    sum += digit **3
    temp //=10
if num==sum:
    print("yes")
else:
    print("no")
