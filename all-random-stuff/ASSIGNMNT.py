def usrinfo(x,y):
    print("Hello " + x + "," + "you are " + str(y) + " years old.")
    print("Next year you will be ", str(y+1))

def smallest(x,y,z):
    RESULT= min(x,y,z)
    return RESULT

def largest(x,y,z):
    RESULT= max(x,y,z)
    return RESULT

def pwr(x,y):
    RESULT= x**y
    print(str(x) + " rasie to the power " + str(y) + " is " + str(RESULT))

def add(x,y):
    RESULT= x+y
    print("The addition of  " + str(x) + " and " + str(y) + " is " + str(RESULT))

def sub(x,y):
    RESULT= x-y
    print("The subtraction of  " + str(x) + " and " + str(y) + " is " + str(RESULT))

def mul(x,y):
    RESULT= x*y
    print("The multiplication of  " + str(x) + " and " + str(y) + " is " + str(RESULT))

def div(x,y):
    RESULT= x/y
    print("The division of  " + str(x) + " and " + str(y) + " is " + str(RESULT))

    
def rem(x,y):
    RESULT= x%y
    print("The modulus of  " + str(x) + " and " + str(y) + " is " + str(RESULT))


def calc(x,y):
    add(x,y)
    sub(x,y)
    mul(x,y)
    div(x,y)
    pwr(x,y)
    rem(x,y)


        
def cstr(a,b,c,d):
    print(a + b + c + d)

def calc_hyp(x,y):
    r = ((x**2) + (y**2))**0.5
    print ("HYPOTENUSE= " + str(r))

def sqr(x):
    SQ= x**2
    print (SQ)
    print (SQ)
    print (SQ)
    print (SQ)
    
#Alternative method
def SQR(x):
    SQ= x**2
    for n in range (4):
        print(SQ)

def ctof(c):
    f= (9.0/5.0)*c+32
    return f
def ftoc(f):
    c= 5.0/9.0*(f-32)
    return c

def temp():
    x= float(input("Enter temperature in calcius: "))
    y= float(input("Enter temperature in fahrenheit: "))
    print(ctof(x))
    print(ftoc(y))

def dist():
    x1= int(input("Enter value for x1: "))
    y1= int(input("Enter value for y1: "))
    x2= int(input("Enter value for x2: "))
    y2= int(input("Enter value for y2: "))

    dist= ((x2-x1)**2 + (y2-y1)**2)**0.5
    print("The distance between points: " + "(" + str(x1) + "," + str(y1) + ")" + " and " + "(" + str(x2) + "," + str(y2) + ")" + " is " + str(dist))
    
