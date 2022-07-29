# Accept number and sort its digits in a list
# accepting
number = input("Enter a number:")
# assigning
number_list = []
# process
for chr in number:
  number_list.append(int(chr))

# ouput
number_list.sort()
print(number_list)



