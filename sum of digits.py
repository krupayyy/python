# Function definition
def sod(num):
  digitsum = 0
  remainder = 0
  # for chr in str(num):
  #     digitsum = digitsum+int(chr)
  while num > 0:
    remainder = num%10
    digitsum = remainder + digitsum
    num = num//10
  return digitsum

# --------------Function definition end
# Function execution
num1 = int(input("Enter a number:"))
num2 = sod(num1)
print(num2)



