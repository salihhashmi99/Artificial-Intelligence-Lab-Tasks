year=float(input("Enter the year : "))
if year%4!=0:
    print("Common year ")
elif year%100!=0:
    print("Leap year ")
elif year%400!=0:
    print("Common year")
else:
    print("Leap year")
if year>=1582:
    print("This year falls in the Gregorian era")
else:
    print("This year not lies within the Gregorian calender era")
