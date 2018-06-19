def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    if n==0:
        return 1
    else:
        return f
def series():
    a=int(input("Enter the number:"))
    n=int(input("Enter the limit:"))
    sum=1
    for i in range(1,n+1):
        sum=sum+(a**i)/fact(i)
    print("Sum of the series is",sum)
series()
