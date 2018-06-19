#Name	:G.Jegadeeswari
#Roll no:17UITE019
#Date   :13.10.2017
#To subtract the two matrix
#Displaying
print "Name:G.Jegadeeswari"
print "Roll no:17UITE019"
print "Date   :13.10.2017"
print "To subtract the two matrix"

#Empty 2D list
a=[]
b=[]
c=[]

#Get input for row limit and column limit
m=input("Enter the row limit:")
n=input("Enter the column limit:")

#Create an empty 2D lists
for i in range(m):
	a.append([])
for i in range(m):
	b.append([])
for i in range(m):
	c.append([])
#Get the element for 2D list
print "Enter the elements of Matrix A"
for i in range(m):
	for j in range(n):
		x=input()
		a[i].append(x)
print "Enter the elements of Matrix B"
for i in range(m):
	for j in range(n):
		y=input()
		b[i].append(y)
#Display the 2D list
print"The Element in the matrix A are"
for i in range(m):
	for j in range(n):
		print format(a[i][j],"4d"),
	print  
print"The Element in the matrix B are"
for i in range(m):
	for j in range(n):
		print format(b[i][j],"4d"),
	print  
#subtracting the two Matrix
for i in range(m):
	for j in range(n):
		r=(a[i][j]-b[i][j])
		c[i].append(r)
#Displaying the Result
print "the subtraction of matrixA and matrixB is"
for i in range(m):
	for j in range(n):
		print (format(c[i][j],"4d")),
	print





















