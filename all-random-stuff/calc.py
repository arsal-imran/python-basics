print("Type " + "calc()" + " and " + "press enter")
def calc():
    a= int(input("Enter your first value: "))
    b= int(input("Enter your second value: "))
    line="---------------------------------------"

    print("1.Add") ; print("2.Subtract") ; print("3.Multiply")
    print("4.Divide") ; print("7.Exponent") ; print("8.Modulus")

    x= int(input("Enter your choice: "))

    if x==1:
        c=a+b
        print("The addition of " + str(a) + " and " + str(b) + " is " + str(c))

    elif x==2:
        c=a-b
        print("The subtraction of " + str(a) + " and " + str(b) + " is " + str(c))

    elif x==3:
        c=a*b
        print("The multiplication of " + str(a) + " and " + str(b) + " is " + str(c))
    
    elif x==4:
        c=a/b
        print("The division of " + str(a) + " and " + str(b) + " is " + str(c))

    elif x==5:
        c=a**b
        print(str(a) + " raise to the power " + str(b) + " is " + str(c))

    elif x==6:
        c=a%b
        print("The modulus of " + str(a) + " and " + str(b) + " is " + str(c))

    print(line)
    print("Do you want to do another calculations? ")
    print("1.Yes / 2. No")
    y= int(input("Enter you choice? "))
    if y==1:
        calc()

    elif y==2:
        print(line)
        print("Thanks for using my program")
        print("Courtesy of: ARSAL IMRAN")
