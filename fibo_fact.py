# def fibo(num):
#     if num==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return(fibo(num-1) + fibo(num-2))
# num=int(input("num: "))
# for n in range(0,num):
#     print(fibo(n))

# n=int(input("your num: "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

def fibo(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return(fibo(num-1)+fibo(num-2))
n=int(input("your num: "))
for n in range(0,n+1):
    print(fibo(n))