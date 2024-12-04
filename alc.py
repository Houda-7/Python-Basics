
years= [2000,2016,2015,2004]
for i in range (10):
    year = int(input("Enter a year :"))
    if year % 400 == 0:
        print(f"{year} is a leap year.")
    elif year % 100 == 0:
        print(f"{year} is not a leap year.")
    elif year % 4 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


