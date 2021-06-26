#This code will count the numbers of integers
def count(m):
    count= 0
    while m>1:
        count = count + 1
        m= m / 10
        
    print(count)
#Alternative method for the above process
def new(n):
    count= 1
    while n>10:
        count= count + 1
        n= n/10
    print(count)

def new1(n):
    count= 0
    while n>0:
        count= count + 1
        x= n%10
        if x>0:
            print(x)
    print(n)

def neww(n):
    count= 1
    while n>10:
        count= count + 1
        n= n%10
    print(count)
