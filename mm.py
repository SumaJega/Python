#Name	:G.Jegadeeswari
#Roll no:17UITE019
#Date   :13.10.2017
#To find the Maximum and Minimum number in the given list
#Displaying
print "Name	:G.Jegadeeswari"
print "Roll no:17UITE019"
print "Date   :13.10.2017"
print "To find the Maximum and Minimum number in the given list"

def mm():
    min=a[0]
    max=a[0]
    for i in range(len(a)):
                if min>a[i]:
                    min=a[i]
                if max<a[i]:
                    max=a[i]
    print "Maximum value in the list is",max
    print "Minimum value in the list is",min
n=input("Enter the limit:")
a=[]
print("Enter the elements")
for i in range(n):
    b=input()
    a.append(b)
mm() 
