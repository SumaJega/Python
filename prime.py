def prime():
    a=int(input("Enter the number:"))
    flag=0
    if a>0:
        for i in range(2,a+1):
            if a%i==0:
                flag=1
            if flag==1:
                return 1
            else:
                return 0
    else:
        return -1
flag=prime()
if flag==1:
    print("Not a prime number")
else:
    print("Prime number")
    
