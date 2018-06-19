#Name: G.Jegadeeswari
#Roll number:17UTE019
#Date:10.11.2017
#To create a student record with rollnumber and name using dictionary
print "Name: G.Jegadeeswari"
print "Roll number:17UTE019"
print "Date:10.11.2017"
print "To search  a student record with rollnumber and display the name "
d={}
n=input("Enter the total strength:")
detail=["Rollnumber","Name"]

for i in range(n):
	d[i]={}
	for key in detail:
		print "Enter the value for ",key,":"
		value=input()
		d[i][key]=value
print d
for i in range(n):
	print "Details of the student",i
	for key in d.get(i):
		print key,":",d[i][key] 
flag=0
s=input("Enter the Searching Roll number:")
for i in range(n):
	if d[i]["Rollnumber"]==s:
		flag=1
		break
if flag==1:
	print"Name of the student:",d[i]["Name"]
else:
	print "Not found"


