"""
HW: 2
Problem: check_isbn
Author:Gudipudi Harikapadmini
"""

def check_even_digits(c):
    """This function finds the even placed digits and multiply by 2 and then sum up all of them """
    even_digits = 0
    for i in c[-2::-2]:
        if int(i) * 2 >= 10:  # if i is more than 10 then modulo by 10
            s = int(i) * 2 % 10 + int(i) * 2 // 10
        else:
            s = int(i) * 2
        even_digits = even_digits+s

    return even_digits


def check_odd_digits(c):
    """This function finds the odd placed digits and sum up them"""
    tot = 0
    for i in c[-1::-2]:
        tot = tot+int(i)

    return tot


if __name__ == '__main__':
    """Prints the credit card is valid or not"""
    while True:
        card = input('Please enter credit card number: ')
        if (13 <= len(card) <= 16) and card.startswith(('4', '5', '37', '6')):
            break
        else:
            print('Your card is invalid/ Does not belongs to a company')
    total = check_odd_digits(card)+check_even_digits(card)
    if total % 10 == 0:
        print("Valid card")
    else:
        print("Invalid card")
