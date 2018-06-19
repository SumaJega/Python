#Empty 2D list
a=[]

#Get input for row limit and column limit
m=input("Enter the row limit:")
n=input("Enter the column limit:")

#Create an empty 2D list
for i in range(m):
	a.append([])

#Get the element for 2D list
print ("Enter the elements")
for i in range(m):
	for j in range(n):
		b=input()
		a[i].append(b)

#Display the 2D list
print("The Element in the matrix are"
for i in range(m):
	for j in range(n):
		print format(a[i][j],"4d"),
	print  

