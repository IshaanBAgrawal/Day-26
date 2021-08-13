with open("file1.txt") as no_list_1:
    list_no_1 = no_list_1.readlines()
list1 = [no[0:len(no) - 1] for no in list_no_1]

with open("file2.txt") as no_list_2:
    list_no_2 = no_list_2.readlines()
list2 = [no[0:len(no) - 1] for no in list_no_2]

result = [int(no1) for no1 in list1 for no2 in list2 if no1 == no2]

# Write your code above 👆

print(result)



