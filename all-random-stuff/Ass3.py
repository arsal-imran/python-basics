'''
Assignment 3
'''
def age(x):
    if x<=18:
        print("Your are young")
    else:
        print("You are old")
def even_odd(x):
    if x%2==0:
        print(str(x) + " is an even number")
    else:
        print(str(x) + " is an odd number")

def triangle(a,b,c):
    if a+b>c or b+c>a or c+a>b:
        print("The triangle is valid")
        A= (1/2)*a*b
        print("The area of triangle is: ", str(A))

    else:
        print("The triangle is invalid")

def rectangle(a,b,c,d):
    if (a==b and c==d) or (a==d and b==c):
        print("The rectangle is valid")
        A= a*c
        print("The area of rectangle is: ", str(A), " sq. units")

    else:
        print("The rectangle is invalid")

def yes(a):
    if a== "Y" or a=="y" or a== "YES":
        print("You choise yes")
    else:
        print("You chose NO")

def sum_odd(a,b,c,d,e):
    SUM=0
    if a%2!=0:
        SUM= SUM+ a
        
    if b%2!=0:
        SUM= SUM+ b
        
    if c%2!=0:
        SUM= SUM+ c
        
    if d%2!=0:
        SUM= SUM+ d
        
    if e%2!=0:
        SUM= SUM+ e

        print("The sum of odd numbers is ", str(SUM))

def count_even_odd(a,b,c,d,e):
    EVEN=0
    ODD=0
    if a%2==0:
        EVEN= EVEN + 1

    else:
        ODD= ODD + 1

    if b%2==0:
        EVEN= EVEN + 1

    else:
        ODD= ODD + 1

    if c%2==0:
        EVEN= EVEN + 1

    else:
        ODD= ODD + 1

    if d%2==0:
        EVEN= EVEN + 1

    else:
        ODD= ODD + 1

    if e%2==0:
        EVEN= EVEN + 1

    else:
        ODD= ODD + 1

    print("EVEN= ", str(EVEN))
    print("ODD= ", str(ODD))

def cb_sqr():
    a=int(input("Enter value for A: "))
    b=int(input("Enter value for B: "))
    c=int(input("Enter value for C: "))
    d=int(input("Enter value for D: "))
    e=int(input("Enter value for E: "))

    if a%2==0:
        print(a**2)
    else:
        print(a**3)

    if b%2==0:
        print(b**2)
    else:
        print(b**3)

    if c%2==0:
        print(c**2)
    else:
        print(c**3)

    if d%2==0:
        print(d**2)
    else:
        print(d**3)

    if e%2==0:
        print(e**2)
    else:
        print(e**3)


def divisions():
    a=int(input("Enter marks for subject A: "))
    b=int(input("Enter marks for subject B: "))
    c=int(input("Enter marks for subject C: "))
    d=int(input("Enter marks for subject D: "))
    e=int(input("Enter marks for subject E: "))

    per= a+b+c+d+e/500

    if per<=60:
        print("First division")

    if per>=50 and per<60:
        print("Secind division")
        
    if per>40 and per<50:
        print("Third division")
    else:
        print("Fail")

def greatest(a,b,c):
    if a>b and b>c:
        print(str(a), " is greatest")

    if a<b and b<c:
        print(str(c), " is greatest")

    else:
        print(str(b)," is greatest")

def temp():
    t=int(input("Enter temperature: "))
    if t<0:
        print("FREEZING")

    if t>0 and t<16:
        print("COLD")

    if t>=16 and t<=30:
        print("WARM")

    if t>30 and t<=40:
        print("HOT")

    if t>40:
        print("VERY HOT")

def add(a,b):
    return a+b

def div(a,b):
    return a/b

def mul(a,b):
    return a*b

def mod(a,b):
    return a%b

def calc():
    x= int(input("Enter your first value: "))
    y= int(input("Enter your second value: "))

    print("1--->add")
    print("2--->divide")
    print("3--->multiply")
    print("4--->modulus")
    choice= int(input("Specify your operation: "))

    if choice==1:
        print("The addition of ",str(x)," and ",str(y), " is ",add(x,y))

    if choice==2:
        print("The division of ",str(x)," and ",str(y), " is ",add(x,y))

    if choice==3:
        print("The multiplication of ",str(x)," and ",str(y), " is ",add(x,y))

    if choice==4:
        print("The modulus of ",str(x)," and ",str(y), " is ",add(x,y))

    else:
        print("Invalid specifier")
        
