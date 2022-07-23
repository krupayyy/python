#Accept number and display whether it is odd or even
number = int(input("Enter number:"))

#When the number is divided by 2, and the remainder is 0, then it is even, else, it is odd
if number % 2  == 0 :
    print("Even")
else:
    print("Odd")
