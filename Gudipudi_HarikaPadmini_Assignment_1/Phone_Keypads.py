"""
HW        # Assignment 1
Problem 3 # Phone keypads
Author    # Gudipudi HarikaPadmini
"""


def get_number(input_str):
    """
    Translates the input string into phone number
    :param input_str:
    :return:
    """
    keypad_map = {
        'a': '2', 'b': '2', 'c': '2',
        'd': '3', 'e': '3', 'f': '3',
        'g': '4', 'h': '4', 'i': '4',
        'j': '5', 'k': '5', 'l': '5',
        'm': '6', 'n': '6', 'o': '6',
        'p': '7', 'q': '7', 'r': '7', 's': '7',
        't': '8', 'u': '8', 'v': '8',
        'w': '9', 'x': '9', 'y': '9', 'z': '9'
    }
    output = ""
    for char in input_str:
        if char.isalpha():
            output = output + keypad_map[char.lower()]
        else:
            output = output + char
    return output


if __name__ == '__main__':
    input_str = input("Please enter keypad string: ")
    output = get_number(input_str)
    print(output)
