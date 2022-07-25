# Accept a number and display whether if it is a perfect number or not
number = int(input("Enter number:"))
# initialization
total = 0
# process
for i in range(1, number // 2 + 1):
    remainder = number % i
    # factor or not and add to total if factor
    if remainder == 0:
        total = total + i
# output
if total == number:
    print("Perfect number")
else:
    print("Not a perfect number")
