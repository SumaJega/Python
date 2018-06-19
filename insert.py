#Name:G.Jegadeeswari
#Roll number:17UTE019
#Date:10.11.2017
#To find the Sorted list for given list using insertion sort
print "Name:G.Jegadeeswari"
print "Roll number:17UTE019"
print "Date:27.10.2017"
print "To find the Sorted list for given list using insertion sort"
a=[]
n=input("Enter the limit:")
print "Enter the elements:"
for i in range(n):
	b=input()
	a.append(b)
print "Before Sorting"
print a
for i in range(1,n):
	t=a[i]
	k=i
	while (k>0) and (t<a[k-1]):
		a[k]=a[k-1]
		k=k-1
	a[k]=t
print "After Sorting"
print "The insertion sorted list"
print a







