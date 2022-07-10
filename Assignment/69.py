#  Python | Convert a list of Tuples into Dictionary

x= [("akash", 10), ("gaurav", 12), ("anand", 14)]

# dict_1 = dict()
#
# for student, score in x:
#     dict_1.setdefault(student,[]).append(score)
# print(dict_1)

print(dict(x))