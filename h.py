a=int(input("Enter the starting number:"))
b=int(input("Enter the ending number:"))
print("Prime Number between the given range:")
for i in range(a,b+1):
	k=0
	for j in range(a, i//2):
		if(i%j==0):
			k=k+1
	if(k<=0):
		print(i)
