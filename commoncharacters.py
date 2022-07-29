# Accept 2 strings and display the common characters
str1 = str(input("Enter a string:"))
str2 = str(input("Enter another string:"))

for chr1 in str1:
    for chr2 in str2:
        if chr2==chr1:
            print(chr2)
            break
            