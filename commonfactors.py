#Accept 2 numbers and display their common factors
num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))

if num1 < num2:
    smallestNumber = num1
else:
    smallestNumber = num2

for i in range(2, smallestNumber // 2 + 1):
    remainder1 = num1 % i
    remainder2 = num2 % i
    if remainder1 == 0 and remainder2 == 0:
        print(i)


