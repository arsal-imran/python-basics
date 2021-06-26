def loop():
    count = 0
    counteven=0
    countodd = 0
    while count<=50:
        x=int(input("Enter a number :"))
        if x%2==0:
            counteven = counteven +1
        else :
            countodd = countodd+1
        count = count+1
    print("No of even nos = " + str(count))
    print("No of odd nos =" + str(countodd))

def loop1():
    count = 0
    Sum=0
    while count<=4:
        x=int(input("Enter a number :"))
        if x%2!=0:
            Sum= Sum+x
        count = count +1
    avg= Sum/count
    print(avg)

def loop2():
    count=1
    x=int(input("Enter a number"))
    while count<=10:
        y=x*count
        print( str(x) + "x" + str(count) + "=" + str(y))
        count = count+1

def loop3():
    count=1
    Sum=1
    x=int(input("Enter a number"))
    while Sum<=1000:
        y=x**count
        print( str(x) + "x" + str(count) + "=" + str(y))
        count= count+999
