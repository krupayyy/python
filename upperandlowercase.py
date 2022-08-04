# Create a function that takes multiple strings and returns the string with the most characters
# Function definition
def largeststring(strlist):
    maxlength = 0
    maxstridx = 0
    counter =  0
    for str in strlist:
        if len(str) > maxlength:
          maxlength = len(str)
          maxstridx = counter
        counter += 1
    return strlist[maxstridx]
# Function execution
strlist1 = ["one","twice","thrice"]
print(largeststring(strlist1))