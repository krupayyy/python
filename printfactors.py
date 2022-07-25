# Accept a number and display its factors
number = int(input("Enter number:"))

for i in range(2,number//2+1):
  remainder = number % i
  if remainder == 0:
    print(i)

