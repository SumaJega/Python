ip=open('Suma.txt','r')
fp=open('Jega.txt','w')
for lines in ip:	
	a=int(lines)
	flag=0
	for i in range(2,a//2+1):
		if a>0:
			if a%i==0:
				flag=1
				break
	if flag==1:
		print a," Not prime"
	else:
		print a," Prime number"


