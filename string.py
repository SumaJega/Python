def strop():
     if ch==1:
          print("Finding Length")
          str1=input("Enter the string:")
          a=len(str1)
          print("Length of the given string:",a)
     elif ch==2:
          print("Concatenation")
          str1=input("Enter the first string:"))
          str2=input("Enter the second string:"))
          a=str1+str2
          print("Concatenation of the two string is:",a)
      elif ch==3:
          print("Multiple Copies")
          str1=input("Enter the string:")
          n=int(input("Enter the no of copies:")
          a=str1*n
          print("Multiple Copies of the given string:",a)
     elif ch==4:
          print("Slicing")
          str1=input("Enter the string:")
          x=int(input("Enter the start index:"))
          y=int(input("Enter the end index:"))
          a=str1[x:y+1]
          print("Slicing:",a)
     elif ch==5:
          print("Comparison")
          str1=input("Enter the first string:")
          str2=input("Enter the second string:"))
          if str1>str2:
               print (str1,"is greater than ",str2)
          else:
               print (str2,"is greater than ",str1)
     elif ch==6:
          print("Reversing")
          str1=input("Enter the string:")
          a=str1[::-1]
          print("The reversed string:",a)
     elif ch==7:
          print("Substring matching")
          str1=input("Enter the string:")
          x=int(input("Enter the middle index of str1:"))
          str2=str1[x:]
          str3=input("Enter the sub string:")
          str4=str3+str2
          print("The substring matching:")
     elif ch==8:
          print("Checking for digit")
          a=input("Enter the string:")
          if a.isdigit():
               print("Only Digit")
          else:
               print("Mixed Character")
     elif ch==9:
          print("Checking for alphabet")
          a=input("Enter the string:")
          if a.isalpha():
               print("Only Alphabets")
          else:
               print("Mixed Character")
     elif ch==10:
          print("Checking alphanumeric")
          a=input("Enter the string:")
          if a.isalnum():
               print("Mixed Character")
          else:
               print("Either Alphabet or Digit")
     elif ch==11:
          print("Uppercase Conversion")
          a=input("Enter the string:")
           if a.isupper():
                print("Upper case")
           else:
                print("Lower case")
     elif ch==12:
          print("Uppercase Conversion")
          a=input("Enter the string:")
          if a.islower():
                print("Lower case")
           else:
                print("Upper case")
     else:
          print("Your choice is Invalid")
print("Menu")
print("String Operations")
print("   1.Finding Length")
print("   2.Concatenation")
print("   3.Multiple Copies")
print("   4.Slicing")
print("   5.Comparison")
print("   6.Reversing")
print("   7.Substring matching")
print("   8.Checking for digit")
print("   9.Checking for alphabet")
print("   10.Checking alphanumeric")
print("   11.Uppercase Conversion")
print("   12.Lowercase Conversion")
ch =int(input("Enter your choice:"))
strop()





