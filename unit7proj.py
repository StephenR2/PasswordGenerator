# Stephen Randall
# 10/31/17
# Folder: Unit7Project File: unit7proj.py
# This is a password generator that generates either a code or a pass phrase.
import random


def passphrase(how_many_words):
    """
    This function deals with creating a passphrase for the user if they chose this option. It opens a file of words and
    reads the file, randomly picks a number of words predefined by the user in "how_many_words" then prints it out.
    Asks user if they'd like to switch out some letters for symbols / numbers if yes it passes the passphrase to the
    substitution function.
    :param how_many_words: Receives the number of words the function should pick out of the text file from the main.
    """
    myfile = open("english3.txt", "r")
    listoffilecontents = myfile.readlines()
    final_pass = ""
    for x in range(how_many_words):
        list_pass = (random.choice(listoffilecontents))
        final_pass = final_pass + list_pass[0:-1]
    print(final_pass)
    substitute_letters = input("Would you like to substitute letters for symbols or numbers? (y/n)")
    if substitute_letters == "y":
        symbol_pass = substitution(final_pass)
        print("Your updated password is:", symbol_pass)
        print("Thanks for using my password generator!")
    else:
        print("Thanks for using my password generator!")


def passcode(how_many_characters):
    """
    Function that determines what your passcode will be, asks you what you want in your passcode and then randomly
    generates it for you.
    :param how_many_characters: param that is received from main, receives how many characters the user wants in their
    passcode.
    """
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers_list = "1234560789"
    symbols_list = ")(@^*&%#-+_="
    choice = ""
    final_passcode = ""
    lower_case_decision = input("Would you like to have lower case letters in your passcode? (y/n)")
    if lower_case_decision == "y":
        choice = choice + lowercase_letters
    else:
        print("Okay, no lower case letters will be included.")
    upper_case_decision = input("Would you like to have upper case letters in your passcode? (y/n)")
    if upper_case_decision == "y":
        choice = choice + uppercase_letters
    else:
        print("Okay, no upper case letters will be included.")
    number_decision = input("Would you like to have numbers in your passcode? (y/n)")
    if number_decision == "y":
        choice = choice + numbers_list
    else:
        print("Okay, no numbers will be included.")
    symbols_decision = input("Would you like to have symbols in your passcode? (y/n)")
    if symbols_decision == "y":
        choice = choice + symbols_list
    else:
        print("Okay, no symbols will be included.")
    for x in range(how_many_characters):
        pick_pass = choice[random.randint(0, len(choice))]
        final_passcode = final_passcode + pick_pass
    print(final_passcode)
    print("Thank you for using my password generator!")


def substitution(final_pass):
    """
    This deals with substituting letters for symbols and numbers that look similar to them. Makes a list of letters and
    another list of corresponding symbols / numbers . Replaces and returns back the new pass.
    :param final_pass: Receives the password that it is editing from the passphrase function.
    :return: returns back the newly edited pass back to passphrase function.
    """
    symbol_pass = ""
    for character in final_pass:
        letters = ["a", "l", "e", "s", "c", "o"]
        symbols = ["@", "!", "3", "5", "(", "0"]
        if character in letters:
            replaced_letter = letters.index(character)
            symbol_pass = symbol_pass + symbols[replaced_letter]
        else:
            symbol_pass = symbol_pass + character
    return symbol_pass


def main():
    print("Press 1 to generate a random password")
    print("Press 2 to generate a pass phrase from random words")
    type_of_password = input("What is your choice (1 or 2)")
    if type_of_password == "2":
        how_many_words = int(input("How many words do you want in the passphrase? please use a number as answer ex: 3"))
        passphrase(how_many_words)
    elif type_of_password == "1":
        how_many_char = int(input("How many characters do you want in the passcode, please answer with an integer!"))
        passcode(how_many_char)
    else:
        print("Okay, Bye.")


main()
