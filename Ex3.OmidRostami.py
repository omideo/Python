year=int(input("Please Enter  a year :"))
if year%4==0 or ( year%4==0 and year%100!=0 ) :
    print("This year is leap year")
else:
    print("This year is not leap year")