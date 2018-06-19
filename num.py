import math 
def numfn():
     ch =int(input("Enter your choice:"))
     if ch==1:
          a=int(input("Enter the number:"))
          print("Ceiling value")
          print("Ceiling value of given number is ",math.ceil(a))
     elif ch==2:
          a=int(input("Enter the number:"))
          print("Flooring value ofgiven number is ",math.floor(a))
     elif ch==3:
          a=int(input("Enter the number:"))
          print("Factorial value of given number is ",math.factorial(a))
     elif ch==4:
          a=int(input("Enter the number:"))
          print("Absolute value of given number is ",math.abs(a))
     else:
          print("Your choice is Invalid")
def powlog():
     ch =int(input("Enter your choice:"))
     if ch==1:
          a=int(input("Enter the number:"))
          print("Exponention value of given number  is ",math.exp(a))
     elif ch==2:
          a=int(input("Enter the number:"))
          print("Logarithmic value of given number is ",math.log10(a))
     elif ch==3:
          a=int(input("Enter the first number:"))
          b=int(input("Enter the second number:"))
          print("Power of value is of given number ",math.pow(a,b))
     elif ch==4:
          a=int(input("Enter the number:"))
          print("Squareroot of given number is ",math.sqrt(a))
     else:
          print("Your choice is Invalid")
def trihy():
     ch =int(input("Enter your choice:"))
     if ch==1:
          a=int(input("Enter the number:"))
          print("Sine value of given number is ",math.sin(a))
     elif ch==2:
          a=int(input("Enter the number:"))
          print("Cosine value of given number is ",math.cos(a))
     elif ch==3:
          a=int(input("Enter the number:"))
          print("Tangent value of given number is ",math.tan(a))
     elif ch==4:
          a=int(input("Enter the number:"))
          print("Hyberbolic Sine value of given number is ",math.sinh(a))
     elif ch==5:
          a=int(input("Enter the number:"))
          print("Hyberbolic Cosine value of given number is ",math.cosh(a))
     elif ch==6:
          a=int(input("Enter the number:"))
          print("Hyberbolic Tangent value of given number is ",math.tanh(a))
     else:
          print("Your choice is Invalid")
def numsy():
     ch =int(input("Enter your choice:"))
     if ch==1:
          a=int(input("Enter the number:"))
          print("Binary Conversion of given number is ",math.bin(a))
     elif ch==2:
          a=int(input("Enter the number:"))
          print("Octal Conversion of given number is ",math.oct(a))
     elif ch==3:
          a=int(input("Enter the number:"))
          print("Hexadecimal Conversion of given number is ",math.hex(a))
     else:
          print("Your choice is Invalid")
print("Menu")
print("1.Number Functions")
print("   1.Ceiling")
print("   2.Flooring")
print("   3.Factorial")
print("   4.Absolute")
print("2.Power and Logarithmic Functions")
print("   1.Exponention")
print("   2.Logarithmic base10")
print("   3.Power of")
print("   4.Squareroot")
print("3.Trignometric and Hyberbolic Functions")
print("   1.Sine value")
print("   2.Cosine value")
print("   3.Tangent value")
print("   4.Hyberbolic Sine value")
print("   5.Hyberbolic Cosine value")
print("   6.Hyberbolic Tangent value")
print("4.Number System")
print("   1.Binary Conversion")
print("   2.Octal Conversion")
print("   3.Hexadecimal Conversion")
ch=int(input("Enter Your Choice:"))
while ch<5:
     if ch==1:
          print("Number Function")
          numfn()
     elif ch==2:
          print("Power and Logarithmic Functions")
          powlog()
     elif ch==3:
          print("Trignometric and Hyberbolic Functions")
          trihy()
     elif ch==4:
          print("Number System")
          numsy()
     else:
          print("Your choice is Invalid")
 


