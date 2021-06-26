print("What do you want to do? ")
print("1. Print string")
print("2. print numeric value")
print("**********************")
x= int(input("Enter your choice:  "))

if x== 1:
    a= input("Enter your string: ")
    n= int(input("How much times you want to do a loop? "))
    for n in range (n):
        print(a)
        
elif x==2:
    a= int(input("Enter a numeric value : "))
    n= int(input("How much times you want to do a loop? "))
    for n in range (n):
        print(a)
        
print("######################")
print("Program Ended - Thanks")
