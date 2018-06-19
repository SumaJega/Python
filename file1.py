#Name:G.Jegadeeswari
#Rollno:17UITE019
#Date:24.11.2017
#To Open and close the files
print"Name:G.Jegadeeswari"
print"Rollno:17UITE019"
print"Date:24.11.2017"
print"To Open and close the file"



#Opening a file
fp=open('io.txt','w')


#After opening the file
print"File name:",fp.name
print"File Status(Closed/Opened)",fp.closed
if fp.closed:
	print "File is Opened"
else:
	print "File is Closed"
print "File Mode",fp.mode


#Closing a file
fp.close()
print "\n\n\n"


#After Closing the File
print "File name:",fp.name
print"File Status(Closed/Opened)",fp.closed
if fp.closed:
	print "File is Opened"
else:
	print "File is Closed"

