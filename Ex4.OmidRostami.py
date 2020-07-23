"""This Program receives day, month and, year for 
computing the date after that code shows us for 
example the date is 65th day of the year with determining
the leap year""" 


""" Receiving Day , Month , Year """

day = int(input("Please Enter Day : "))
month = int(input("Please Enter Month : "))
year = int(input("Please Enter year : "))

month_list_regular=[31,28,31,30,31,30,31,31,30,31,30,31]
month_list_leapyear=[31,29,31,30,31,30,31,31,30,31,30,31]


""" For determining that the year is Leap Year or not and calculating date"""


if year%4==0 or ( year%4==0 and year%100!=0 ) :
    num = sum(month_list_leapyear[:month-1]) + day
    print ("This year is leap year and this date is",num,"th day of year.")
else:
    num = sum(month_list_regular[:month-1]) + day
    print ("This year is not leap year and this date is",num,"th day of year.")
