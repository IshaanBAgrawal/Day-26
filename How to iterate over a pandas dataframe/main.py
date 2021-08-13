import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

# for (key, value) in student_dict.items():
#     print(key)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# # Looping through a DataFrame
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)
#     print()

# Loop through the rows of a DataFrame
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)
