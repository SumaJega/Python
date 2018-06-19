#Name:G.Jegadeeswari
#Rollno:17UITE019
#Date:24.11.2017
#To Open and close the files
print"Name:G.Jegadeeswari"
print"Rollno:17UITE019"
print"Date:24.11.2017"
print"To read the content from the user and write it into the file"




fp=open('names.txt','w')
i=input("Enter the contents:")
fp.write(i)

