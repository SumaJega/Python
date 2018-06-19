def get_range(g):
	r=input("Enter the no of rows of Matrix "+g+" : ")
	c=input("Enter the no of columns of Matrix "+g+" : ")
	return r,c
def get_mat(g):
	a=[]
	m,n=get_range(g)
	print "Enter the elements of ",g," Matrix"
	for i in range(m):
		a.append([])
	for i in range(m):
		for j in range(n):
			a[i].append(input())
	return a
def mat_pro(a,b):
	if(len(a[0])==len(b)):   
		for i in range(len(a)):
			for j in range(len(b[0])):	
				for k in range(len(b)):
					c[i][j]+=a[i][k]*b[k][j]
		mat_disp(c,len(a),len(b[0]),'PRODUCT')
	else :
		print "Matrix Multiplication is not possible" 
def mat_disp(a,m,n,g):
	print "The ",g," Matrix is..."
	for i in range(m):
		for j in range(n):
			print format(a[i][j],"4d"),
		print
a=get_mat('A')
b=get_mat('B')
mat_disp(a,len(a),len(a[0]),'A')
mat_disp(b,len(b),len(b[0]),'B')
mat_pro(a,b)
