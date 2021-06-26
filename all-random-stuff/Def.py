def add():
    x=3
    y=4
    sum=x+y
    print (sum)

def pct():
    M1= int(input ("Enter marks for Subject1= "))
    M2= int(input ("Enter marks for Subject2= "))
    M3= int(input ("Enter marks for Subkect3= "))

    SUM= M1+M2+M3
    print ("Total Marks= " + str(SUM))
    PER= (SUM/300)*100
    print ("Your percentage= " + str(PER))

def temp():
    c = int (input("Give temperature in centrigrade=  "))
    f = ((9/5)*c) + 32

    print("The given temperature in Fahreheit is= " + str(f))
