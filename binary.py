#Name	:G.Jegadeeswari
#Roll no:17UITE019
#Date   :13.10.2017
#To find the element in the list using the binary Search
#Displaying
print("Name:G.Jegadeeswari")
print("Roll no:17UITE019")
print("Date   :13.10.2017")
print("To find the element in the list using the binary Search")
def binary():
	s=input("Enter the Search element:")
	flag=0
	start=0
	end=len(a)-1
	mid=0	
	while start<=end:
		mid=(start+end)//2
		if s==a[mid]:
			print ("The Element is Found")
			flag = 1
			break
		elif s>a[mid]:
			start=mid+1
		else:
			end=mid-1
	if flag==0:
		print ("The given Element is Not Found"	)
n=input("Enter the limit:")
a=[]
print("Enter the elements")
for i in range(n):
    b=input()
    a.append(b)
binary()
