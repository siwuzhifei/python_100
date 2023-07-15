alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(en_text, en_shift):
    cipher_text = ""
    for i in range(0, len(en_text)):
        letter = en_text[i]
        position = alphabet.index(letter)
        shift_letter = alphabet[position + en_shift]
        cipher_text += shift_letter
    print(f"The encoded text is {cipher_text}")
    # TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(de_text, de_shift):
    ori_text = ""
    for i in range(0, len(de_text)):
        letter = de_text[i]
        position = alphabet.index(letter)
        de_letter = alphabet[position - de_shift]
        ori_text += de_letter
    print(f"The decoded text is {ori_text}")


    # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
    # e.g.
    # cipher_text = "mjqqt"
    # shift = 5
    # plain_text = "hello"
    # print output: "The decoded text is hello"

    # TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
    #  Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
    encrypt(en_text=text, en_shift=shift)
elif direction == "decode":
    decrypt(de_text=text, de_shift=shift)