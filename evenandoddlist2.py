# Accept numbers from user and print even numbers first, odd numbers next
# assigning
number = int(input("Enter a number[0 to stop]:"))
number_list1 = []
number_list2 = []
# process
while number != 0:
 if number % 2 == 0:
  number_list1.append(number)
 if number % 2 != 0:
  number_list2.append(number)
 number = int(input("Enter a number[0 to stop]:"))

number_list1.sort()
number_list2.sort()
#output
print(number_list1)
print(number_list2)

