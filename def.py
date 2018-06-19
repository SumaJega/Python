n=int(input("Enter the limit:"))
a=[]
print("Enter the elements")
for i in range(n):
    b=int(input())
    a.append(b)
def mm():
    min=a[0]
    max=a[0]
    for i in range(len(a)):
                if min>a[i]:
                    min=a[i]
                if max<a[i]:
                    max=a[i]
    print("Maximum value is",max)
    print("Minimum value is",min)
mm()
