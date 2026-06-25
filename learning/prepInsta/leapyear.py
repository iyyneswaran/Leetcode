year = int(input())

if (year%400 == 0) or (year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# Ternary operator
def is_leap_year(year):
    return True if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else False

year = int(input())
print(f"{year} is a leap year: {is_leap_year(year)}")

# calender module 
import calendar
def calender_leapyear(year):
    return calendar.isleap(year)

print(calender_leapyear(int(input())))


# Lambda function to check leap year
is_leap_year = lambda year: True if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else False

year = int(input())
print(f"{year} is a leap year: {is_leap_year(year)}")