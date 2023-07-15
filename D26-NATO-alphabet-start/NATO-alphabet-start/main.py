
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
alfa_dic = data.set_index("letter")["code"].to_dict()
# phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(alfa_dic)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#is_on = True
#while is_on :

def generate_phonetic():
    in_word = input("Enter a word ：").upper()
    try:
        out_word = [alfa_dic[letter] for letter in in_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(out_word)
        #is_on = False

generate_phonetic()


