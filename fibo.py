
# import calendar
# year=2023
# month=12
# x=calendar.month(year,month)
# print(x)

def fibo(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return (fibo(num-1) + fibo(num-2))
n=int(input("your num: "))
for n in range(0,n):
    print(fibo(n))