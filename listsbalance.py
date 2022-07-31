# # Take 2 lists, first more values than 2nd, once values stop corresponding, print asterisk(*) for 2nd list
# list1 = input("Enter a list:")
# list2 = input("Enter another list:")
# list1 = [1,2,3,4,5,10,15]
# list2 = [5,6,7,8]
list1 = 'Abcjdhksjfhak'
list2 = 'xyldfsj'
diff = len(list1) - len(list2)
for i in range(1,diff+1):
    list2 = list2 + "."
for fv,sv in zip(list1,list2):
    print(fv,sv)