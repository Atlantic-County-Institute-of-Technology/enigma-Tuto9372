# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: YOUR_NAME_HERE
# created: MM.DD.YYYY
# last update:  MM.DD.YYYY
import random

# we'll be using this string for the majority of our translations
alphabet = "abcdefghijklmnopqrstuvwxyz"

# user inputs a message and selects a key (or random), the message is then translated using the cipher
def encode_message():
    msg= input("Type the message you'd like to encode").lower()
    key= int(input("Input the encoding amount"))
    output = ""
    for char in msg:
        msg_char= alphabet[(alphabet.index(char)+key) % 26]
        output += msg_char
    print(f"{msg} now been encoded to {output}")
    fileyn = input("would you like to encode this message into a file?").lower()
    if fileyn == "yes":
        filename = input("what you wanna name it?")
        f = open(f"{filename}.txt", "w")
        f.write(output)
        f.close()
# encodes a target file, similarly to encode_message, except now targeting a filename
def encode_file():
    filename = input("whats the name of the file you would like to encode?").lower()    # user says the file name of the text files they've created
    key = int(input("Input the encoding amount"))   # This is how much it shifts the letter by
    f = open(f"{filename}", "r")  # this specifies which files to grab the data from
    msg = f.read()  # This is what stores the text from said file
    output = ""  # This is just a blank thing to put the encoded text into
    for char in msg: # For each character in the text file
        msg_char = alphabet[(alphabet.index(char) + key) % 26] # takes each char and shifts them by the key amount
        output += msg_char # this just adds the encoded text to output
    print(f"{msg} now been encoded to {output}")# this prints the encoded message
    fileyn = input("would you like to encode this message into a file?").lower()
    if fileyn == "yes":
        filename = input("what you wanna name it?")
        f = open(f"{filename}.txt", "w")
        f.write(output)
        f.close()
# decodes target file using a user-specified key. If key is unknown, a keypress should
# call decode_unknown_key()
def decode_file():
    filename =input("whats the name of the file you would like to decode?").lower()    # user says the file name of the text files they've created
    userans =input("do you know the decoding amount/Key?")
    if userans == "yes":
        key = int(input("Input the DECODING amount"))   # This is how much it shifts the letter by
        f = open(f"{filename}", "r")
        msg = f.read()
        output = ""
        for char in msg:
            msg_char = alphabet[(alphabet.index(char) - key) % 26] # takes each char and shifts them backwards by the key amount
            output += msg_char # this just adds the encoded text to output
        print(f"{msg} now been DECODED to {output}")# this prints the decoded message
        fileyn = input("would you like to DECODE this message into a file?").lower()
        if fileyn == "yes":
            filename = input("what you wanna name it?")
            f = open(f"{filename}.txt", "w")
            f.write(output)
            f.close()
    else:
        decode_unknown_key(filename)
# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key(filename):
    f = open(f"{filename}", "r")
    msg = f.read()
    output = ""
    for key in range(26):
        output = ""
        for char in msg:
            msg_char = alphabet[
                (alphabet.index(char) - key) % 26]  # takes each char and shifts them backwards by the key amount
            output += msg_char  # this just adds the encoded text to output
        print(f"{msg} now been DECODED to {output}+{key}")  # this prints the decoded message
    fileyn = int(input("which key is right?")).lower()
        filename = input("what you wanna name it?")
        f = open(f"{filename}.txt", "w")
        f.write(output)
        f.close()


# main method declaration
def main():
    while True:
        print(f"Welcome to the Enigma Machine!\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode file.\n"
              f"[3]: Decode file.\n"
              f"[4]: Exit.")

        selection = input("Choose an option:")

        if selection == "1":
            encode_message()
        elif selection == "2":
            encode_file()
        elif selection == "3":
            decode_file()
        elif selection == "4":
            print("Goodbye.")
            exit()
        else:
            print("Invalid choice. Please try again.")

# runs on program start
if __name__ == "__main__":
    main()