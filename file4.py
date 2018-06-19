#Name:G.Jegadeeswari
#Rollno:17UITE019
#Date:24.11.2017
#To Open and close the files
print"Name:G.Jegadeeswari"
print"Rollno:17UITE019"
print"Date:24.11.2017"
print"To copy the content from file"
try:
	ip=open('names.txt','r')
	fp=open('Program.txt','w')
	for lines in ip:
		print lines
		fp.write(lines)
except IOError:
	print "File is not found"


