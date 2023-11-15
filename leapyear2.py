import datetime
y1=int(input("enter the starting year="))
y2=int(input("enter the the end year="))
if y1>y2:
    print("end year must be greater than or equal to start year")
else:
    print(f"Leap years from {y1} to{y2}")
    for year in range(y1,y2+ 1):
        if(year % 4 == 0 and year % 100 !=0)or(year % 400==0):
            print(year)
    
