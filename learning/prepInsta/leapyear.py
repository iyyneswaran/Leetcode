year = int(input())

if (year%400 == 0) or (year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# or 
def is_leap_year(year):
    return True if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else False

year = int(input())
print(f"{year} is a leap year: {is_leap_year(year)}")