# Accept 5 numbers and display total (ignore invalid numbers)
i = 0
total = 0
while i < 5:
#Exception Handling
 try:
    num = int(input("Enter number:"))
    i = i + 1
    total = total + num
 except ValueError:
    print("Invalid Number!")

# Execution
print(total)


