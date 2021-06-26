'''
This funtion will tell if the given number is even or odd
'''

def even_odd():
    
    n = int(input("Enter a number "))
    if (n)%2==0:
        print ("The given number is an even number ")

    else:
        print ("The given number is an odd number ")

''''
This function will tell which value is greater
''''

def grt_les():
    a= int(input("Enter your first value: "))
    b= int(input("Enter your second value: "))

    if a>b:
        print (str(a), "is grater ")

    elif a<b:
        print (str(b) + "is greater ")

    else:
        print("Both are equal")


