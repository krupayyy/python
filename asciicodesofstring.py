# Accept a string from user and display ascii codes from string
# accepting
str1 = input("Enter string:")
str1_list = []
# process
for chr in str1:
    str1_list.append(ord(chr))
# output
print(str1_list)


