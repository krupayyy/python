# Accept a sentence and display character number of space
#accepting
sentence = str(input("Enter a sentence:"))
#assigning
countchr = 0

#process
for chr in sentence:
    countchr += 1
    #output
    if chr == ' ':
          print(countchr)
