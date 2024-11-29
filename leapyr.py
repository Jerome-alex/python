import datetime

current_year = datetime.datetime.now().year

years_input = input(f"Enter a list of years after {current_year}, separated by spaces: ")

years = [int(year) for year in years_input.split()]

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

future_leap_years = [year for year in years if year >= current_year and is_leap_year(year)]

if future_leap_years:
    print("Future leap years:", future_leap_years)
else:
    print("No leap years found in the entered years.")

