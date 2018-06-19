#Name:G.Jegadeeswari
#Roll number:17UTE019
#Date:27.10.2017
#To find the Sorted list for given list using selection sort
print "Name:G.Jegadeeswari"
print "Roll number:17UTE019"
print "Date:27.10.2017"
print "To find the Sorted list for given list using selection sort"
a=[]
n=input("Enter the limit:")
print "Enter the elements:"
for i in range(n):
	b=input()
	a.append(b)
print "Before Sorting"
print a
for i in range(0,len(a)):
	small=i	
	for j in range((i+1),len(a)):
		if a[j]<a[small]:
			small=j
	t=a[small]
	a[small]=a[i]
	a[i]=t
print "After Sorting"
print "The selection sorted list"
print a
