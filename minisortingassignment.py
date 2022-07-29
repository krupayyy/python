# Accept numbers from user and sort in order, ignore duplicates
# assigning
number = 1
number_list = []
uniquenumber_list = []
# process
while number != 0:
 number = int(input("Enter a number[0 to stop]:"))
 if number != 0 or number != number:
  number_list.append(number)

for chr in number_list:
 if uniquenumber_list.count(int(chr)) == 0:
   uniquenumber_list.append(int(chr))
# output
uniquenumber_list.sort()
print(uniquenumber_list)
