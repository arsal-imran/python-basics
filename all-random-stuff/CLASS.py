def num():
    
    x= int(input("Enteer a number: "))
    if x%5==0:
        y= x**2
        print(str(y))
    
    else:
        y= x**3
        print(str(y))
def lar(x,y):
    if x>y:
        return x
    else:
        return y

def count_odd(a,b,c,d,e):
    SUM= 0
    if a%2!=0:
        SUM= SUM+1
    if b%2!=0:
        SUM= SUM+1
    if c%2!=0:
        SUM= SUM+1
    if d%2!=0:
        SUM= SUM+1
    if e%2!=0:
        SUM= SUM+1

    print(str(str(SUM)))

def count_even_odd(a,b,c,d,e):
    ODD= 0
    EVEN=0
    if a%2==0:
        ODD= ODD+1
    else:
        EVEN= EVEN+1
    if b%2==0:
        ODD= ODD+1
    else:
        EVEN= EVEN+1
    if c%2==0:
        ODD= ODD+1
    else:
        EVEN= EVEN+1
    if d%2==0:
        ODD= ODD+1
    else:
        EVEN= EVEN+1
    if e%2==0:
        ODD= ODD+1
    else:
        EVEN= EVEN+1

    print("Even: ", EVEN)
    print("ODD: ", ODD)

def fn(a,b,c,d,e):
    if (a+b+c+d+e)%2==0:
        ANS= a+b+c+d+e
        print(str(ANS))
    else:
        ANS= a*b*c*d*e
        print(str(ANS))

def vowel(x):
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="o":
        return true
    else:
        return false

     
        
