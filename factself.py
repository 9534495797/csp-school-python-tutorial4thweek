# n=int(input("your num: "))
# fact=1
# for i in  range(1,n+1):
#     fact=fact*i
# print(fact)


def fact(n):
    if n<=0:
        return 1
    else:
        return n*fact(n-1)
n=int(input())
print(fact(n))

