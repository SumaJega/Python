#Name:G.Jegadeeswari
#Roll number:17UTE019
#Date:27.10.2017
#To do the Matrix multiplication
print "Name:G.Jegadeeswari"
print "Roll number:17UTE019"
print "Date:27.10.2017"
print "To do the Matrix multiplication"
a=[]
b=[]
c=[]
m=input("Enter the no of rows of Matrix:")
n=input("Enter the no of columns of Matrix:")
for i in range(m):
	a.append([])
for i in range(m):
	b.append([])
for i in range(m):
	c.append([])
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
print "The Elements of matrix A"
for i in range(m):
	for j in range(n):
		print format(a[i][j],"4d"),
	print
print "The Elements of matrix B"
for i in range(m):
	for j in range(n):
		print format(b[i][j],"4d"),
	print
if(len(a[0])==len(b)):
	for i in range(len(a)):
		for j in range(len(b[0])):	
			res=0
			for k in range(len(a)):
				res+=a[i][k]*b[k][j]
			c[i].append(res)
	print "The Multiplication of matrix A and matrix B"
	for i in range(m):
		for j in range(n):
			print format(c[i][j],"4d"),
		print
else :
	print "Matrix Multiplication is not possible" 

