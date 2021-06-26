def usrinfo():
    a= input("Enter your GOOD NAME? ")
    b= input("Enter your DATE OF BIRTH? ")
    c= input("Your job? ")
    print (" ")
    print (" <Profile Header>")
    print (a)
    print ("Date of birth: " + b)
    print ("Job: " + c)
    
def add():
    x= int(input("Enter first value: "))
    y= int(input("Enter second value: "))
    A= x+y
    print("The addition of " + str(x) + " and " + str(y) + " is " , A)

def subtr():
    x= int(input("Enter first value: "))
    y= int(input("Enter second value: "))
    A= x-y
    print("The subtraction of " + str(x) + " and " + str(y) + " is " , A)

def mltp():
    x= int(input("Enter first value: "))
    y= int(input("Enter second value: "))
    A= x*y
    print("The multiplication of " + str(x) + " and " + str(y) + " is " , A)

def div():
    x= int(input("Enter first value: "))
    y= int(input("Enter second value: "))
    A= x/y
    print("The division of " + str(x) + " and " + str(y) + " is " , A)

def sqr():
    x= int(input("Enter first value: "))
    A= x**2
    print("The square of " + str(x) + " is " , A)

def pwr():
    x= int(input("Enter number: "))
    y= int(input("Raise to the power? "))
    A= x**y
    print(str(x) + " rasie to the power " + str(y) + " is " , A)

def sqrt():
    x= int(input("Enter the number: "))
    A= (x)**(1/2)
    print("The square root of " + str(x) + " is " , A)

def cbrt():
    x= int(input("Enter the number: "))
    A= (x)**(1/3)
    print("The cube root of " + str(x) + " is " , A)
    
def rptstr():
    x= input("Write the sting to be repeated ---> ")
    y= int(input ("How many times you want to repeat the string? "))
    z= x*y
    print (z)
    
    


                
