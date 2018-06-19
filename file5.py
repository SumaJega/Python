#Name:G.Jegadeeswari
#Rollno:17UITE019
#Date:24.11.2017
#To Open and close the files
print"Name:G.Jegadeeswari"
print"Rollno:17UITE019"
print"Date:24.11.2017"
print"To count the number of words in the file"
try:
	l1=0
	ip=open('names.txt','r')
	fp=open('Program.txt','w')
	for lines in ip:
		print lines
		fp.write(lines)
		res=lines.split()
		l1=l1+len(res)
		print res
	print "Number of words in the file is  ",l1
except IOError:
	print "File is not Found"
