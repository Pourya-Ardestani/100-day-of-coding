# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}\
import pandas


def find(word):
    for (key, value) in alfa_dict.items():
        if word == key:
            return value


# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
alfa_df = pandas.read_csv("nato_phonetic_alphabet.csv")
alfa_dict = {row.letter: row.code for (index, row) in alfa_df.iterrows()}
print(alfa_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
# print(list_user)
result = [find(word) for word in user_input]
for word in user_input:
    temp = [value for (key, value) in alfa_dict.items() if word == key]
print(result)
