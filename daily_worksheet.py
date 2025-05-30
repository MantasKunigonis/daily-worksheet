# Welcome.
from datetime import date
today = date.today()
today = today.strftime("%m/%d/%y")
print("Daily Worksheet For", today)

# Space.
print("\n")

# Input phone minutes.
phone_minutes = float(input("Enter Phone Minutes: "))

# Input additional phone minutes.
x = phone_minutes
while x > 0:
    x = input("Enter Phone Minutes: ")
    if x == "":
        x = 0
    else:
        x = float(x)
    phone_minutes += x
print("\t")

# Convert total phone minutes to phone hours.
phone_hours = phone_minutes/60
phone_hours = round(phone_hours,2)

# Input number of calls.
calls = int(input("Enter Number Of Calls: "))

# Space.
print("\t")

# Display phone hours.
print("Total Phone Hours: ", phone_hours)

# Display number of calls.
print("Calls: ", calls)

# Display number of calls per hour.
calls_per_hour = round(calls/phone_hours,2)
print("Calls Per Phone Hour: ", calls_per_hour)

# Keep program open.
input()