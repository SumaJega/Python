#Name:G.Jegadeeswari
#Roll number:17UTE019
#Date:27.10.2017
#To find the Sorted list for given list using bubble sort
print "Name:G.Jegadeeswari"
print "Roll number:17UTE019"
print "Date:27.10.2017"
print "To find the Sorted list for given list using bubble sort"
a=[]
n=input("Enter the limit:")
print "Enter the elements:"
for i in range(n):
	b=input()
	a.append(b)
print "Before Sorting"
print a
for i in range(0,n):
	for j in range(0,n):
		if a[i]<a[j]:
			t=a[i]
			a[i]=a[j]
			a[j]=t
print "After Sorting"
print "The Bubble sorted list"
print a
