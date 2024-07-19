year = int(input("Enter the year you would like to check: "))
if year % 400 == 0:
    print(f"The year {year} is a leap exityear")
elif year % 4 == 0 and year % 100 != 0:
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year")