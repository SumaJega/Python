#Name: G.Jegadeeswari
#Roll number:17UTE019
#Date:10.11.2017
#To get inputfrom the command line from user
print "Name: G.Jegadeeswari"
print "Roll number:17UTE019"
print "Date:10.11.2017"
print "To get inputfrom the command line from user"
import sys
a=input("Enter the element to find the index of the element:") 
print sys.argv[a]
print "The number of words given through command line:"
print (len(sys.argv)-1)

