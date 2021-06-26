def prctg():
    M1= int(input("Enter marks for subject 1: "))
    M2= int(input("Enter marks for subject 2: "))
    M3= int(input("Enter marks for subject 3: "))
    M4= int(input("Enter marks for subject 4: "))
    M5= int(input("Enter marks for subject 5: "))
    
    T1=int(input("Enter total marks for subject 1: "))
    T2=int(input("Enter total marks for subject 2: "))
    T3=int(input("Enter total marks for subject 3: "))
    T4=int(input("Enter total marks for subject 4: "))
    T5=int(input("Enter total marks for subject 5: "))
    
    TO= M1+M2+M3+M4+M5
    TA= T1+T2+T3+T4+T5

    prc= (TO/TA)*100
    print("Your percentage is: ", str(prc))

