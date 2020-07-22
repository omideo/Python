year=int(input("Please Enter  a year :"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap Year")
        else:
            print("Is not Leap Year")
    else:
        print("Is not Leap Year")
else:
    print("Is not Leap Year")
