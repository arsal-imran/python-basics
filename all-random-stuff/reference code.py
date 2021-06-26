def add():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    Sum = x+y
    print(Sum)




    
def userinfo():
    name = input("What is your name?")
    print("Hello " + name)

    job = input("What is your job?")
    print("your job is " + job)

    num = input("Give me your number?")
    print("You said: " + str(num))

    print("End")




def percentage():
    a = int(input("Enter marks in subject 1: "))
    b = int(input("Enter marks in subject 2: "))
    c = int(input("Enter marks in subject 3: "))

    Sum = a+b+c
    print("Your total marks are: ")
    print(Sum)

    print("Do you want to calculate percentage?")
    print("Type '1' for yes")
    print("Type '2' for no")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        d = int(input("Enter total marks: "))    
        percentage = (Sum/d)*100
        print("Your percentage = ")
        print(percentage)
        print("Program End - Thanks")
        
    elif choice == 2:
        print ("Program End - Thanks")





def Temperature():
    c = int(input("Enter temp in C:"))
    f = ((1.8)*c) + 32
    print (" Temp in F is: ")
    print (f)
