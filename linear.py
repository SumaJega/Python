#Name	:G.Jegadeeswari
#Roll no:17UITE019
#Date   :13.10.2017
#To find the element in the list using the Linear Search
#Displaying
print "Name	:G.Jegadeeswari"
print "Roll no:17UITE019"
print "Date   :13.09.2017"
print "To find the element in the list using the Linear Search"

def linear():
	flag=0
	s=input("Enter the Search Element:")
	for i in range(len(a)):
		if s==a[i]:
			print "The Element is Found"
			flag=1
			break
	if flag==0:
		print "The Element is not Found"
n=input("Enter the limit:")
a=[]
print("Enter the elements")
for i in range(n):
    b=input()
    a.append(b)
linear()
