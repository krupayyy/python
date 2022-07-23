# Accept month number and display how many days it has
month = int(input("Enter month number:"))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("This month has 31 days.")
elif month == 2:
    print("This month has 28 days.")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("This month has 30 days.")
else:
    print("Invalid month")
