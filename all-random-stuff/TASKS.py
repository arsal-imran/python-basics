'''
Lab tasks
'''

def age():
    age= int(input("Enter your age: "))

    if age > 18:
        print("You are old")

    else:
        print("you are young")


def even_odd(x):
    if x%2==0:
        print("The number your entered: " + str(x) + " is an even number")

    else:
        print("The number you entered: " + str(x) + " is an odd numner")

def triangle(a,b,c):
    if a+b>c and b+c>a and c+a>b:
        print("The triangle is valid")
        A= 1/2* (b*c)
        print ("Area= ", A, " Sq. Unit")
    else:
        print("The triangle is invalid")

def rectangle(a,b,c,d):
    if (a==b and c==d) or (a==d and b==c):
        print("The rectangle is valid")

    else:
        print("The rectangle is invalid")

def sum(a,b,c,d,e):
    SUM= a+b+c+d+e
    print(str(SUM))

def sumif_odd(a,b,c,d,e):
    if a%2!=0:
        v= int(a)
    else:
        v=0

    if b%2!=0:
        w= int(b)
    else:
        w=0


    if c%2!=0:
        x= int(c)
    else:
        x=0


    if d%2!=0:
        y= int(d)
    else:
        y=0


    if e%2!=0:
        z= int(e)
    else:
        z=0

    SUM= v+w+x+y+z
    print(str(SUM))

def sum_all_even(a,b,c,d,e):
    if a%2==0 and b%2==0 and c%2==0 and d%2==0 and e%2==0:
        sum= a+b+c+d+e
        print(str(sum))
    else:
        print("The sum can't be calculated.")
