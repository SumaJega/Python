#Name: G.Jegadeeswari
#Roll number:17UTE019
#Date:10.11.2017
#To illustrate Tuple operations
print "Name: G.Jegadeeswari"
print "Roll number:17UTE019"
print "Date:10.11.2017"
print "To illustrate Tuple operations"
#Getting input from user for tuple
print "\n\nGetting input from user for tuple"
print"--------------------------------------"
print"Tuple 1"
l1=[]
n1=input("Enter the limit:")
print "Enter the elements:"
for i in range(n1):
	l1.append(input()) 
t1=tuple(l1)
print "Elements in tuple1"
print t1
print "\n\nTuple 2"
l2=[]
n2=input("Enter the limit:")
print "Enter the elements:"
for i in range(n2):
	l2.append(input())
t2=tuple(l2)
print "Elements in tuple2"
print t2
print "\n\nFinding the length of the tuple"
print"-----------------------------------"
#Finding the length of the tuple
len1=len(t1)
len2=len(t2)
print "The Length of the first tuple:",len1
print "The Length of the second tuple:",len2
print "\n\nConcatenate two tuples"
print"---------------------------"
#Concatenate two tuples
t=t1+t2
print "The Concatenated tuple is",t
print "\n\nSlicing or Indexing"
print"-------------------------"
#Slicing or Indexing
print "Results of slicing"
print t[:]
print t[1:]
print t[:-2]
print t[::-1]
print "\n\nRepeatation for n times"
print"----------------------------"
#Repeatation for n times
n=input("Enter the number of times:")
t=t1*n
print "Repeated tuple:", t
print "\n\nComparing two tuple"
print"------------------------"
#Comparing two tuple
if t1>t2:
     print "t1 is greater than t2"
else:
     print "t2 is greater than t1"
print"\n\nMembership operators"
print"------------------------"
#Membership operators
print "The  Elements in t1 are"
for ele in t1:
     print ele
print "The  Elements in t2 are"
for i in range(len2):
     print t2[i]
print "\n\nSearching a element in tuple"
print"---------------------------------"
#Searching a element in tuple
s=input("Enter the search element:")
if s in t1:
     print "Element is Found"
else:
     print "Element is Not Found"
print"\n\nFinding the Maximum and Minimun element in tuple"
print"----------------------------------------------------"
#Finding the Maximum and Minimun element in tuple
m=max(t1)
n=min(t1)
print "The Maximum Element in t1",m
print "The Minimum Element in t1",n
print "\n\nFinding the index "
print"----------------------"
#Finding the index 
a=input("Enter the element which index is to be Found :")
print "Index of",a,"in t1 is",t1.index(a)
print "\n\nCouting the Occurances "
print"--------------------------"
#Couting the Occurances 
b=input("Enter the element to be counted :")
print "Number of occurances of",b,"in t is",t.count(b)
print "\n\nDeleting the tuple"
print"----------------------"
#Deleting the tuple
print "Before Deleting t=",t
del t
print "After Deleting t=",t

