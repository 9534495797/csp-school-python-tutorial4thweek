# n=int(input("your num: "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# def fibo(num):
#     if num==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return (fibo(num-1)+fibo(num-2))
# n=int(input("your num: "))
# for n in range(0,n):
#     print(fibo(n),end='')
def fact(num):
    if num<=1:
        return 1
    else:
        return(num*fact(num-1))
n=int(input("num: "))
print(fact(n))
