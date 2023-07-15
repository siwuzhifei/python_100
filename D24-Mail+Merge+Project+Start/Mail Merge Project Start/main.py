#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
with open("./Input/Letters/starting_letter.txt") as file:
    letter_contents = file.read()

with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

for real_name in name_list:
    stripped_name = real_name.strip()
    new_letter = letter_contents.replace("[name]", stripped_name)
    # the code need to learned
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)







    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp