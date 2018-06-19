#Name:G.Jegadeeswari
#Rollno:17UITE019
#Date:24.11.2017
#To Open and close the files
print"Name:G.Jegadeeswari"
print"Rollno:17UITE019"
print"Date:24.11.2017"
print"To read the content and display the file"
try:
	ip=open('names.txt','r')
	for lines in ip:	
		print lines
except IOError:
	print "File not found" 
