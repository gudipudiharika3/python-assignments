import random

"""
HW: 2
Problem: Hangman
Author:Gudipudi Harikapadmini
"""


def get_hangman(wrd, asterisk_string, guess):
    """This function checks weather the guess is correct or not"""
    count = 0
    asterisk_string = list(asterisk_string)
    for i in range(len(wrd)):
        if wrd[i] == guess:
            asterisk_string[i] = guess
            count = count + 1
    return ''.join(asterisk_string), count


if __name__ == '__main__':
    """This main function takes the random value from the list and prints the replaced letters by asterisk"""
    words = ['Harika', 'naag', 'sanju', 'harshi', 'anath']
    while True:
        wrd = random.choice(words)
        i = 0
        missed = 0
        asterisk_string = '*' * len(wrd)
        input_list = []
        while i < len(wrd):
            guess = input("(Guess) Enter a letter in word " + asterisk_string + '> ')
            if guess in asterisk_string:
                print(guess + " is already in the word")
                continue
            elif guess not in wrd:
                print(guess + " is not in the word")
                missed = missed + 1
                continue
            asterisk_string, count = get_hangman(wrd, asterisk_string, guess)
            i = i + count

        print("The word is " + wrd + ". You missed " + str(missed) + " time")
        new_input = input("Do you want to guess another word? Enter y or n> ")
        if new_input == "n":
            break
