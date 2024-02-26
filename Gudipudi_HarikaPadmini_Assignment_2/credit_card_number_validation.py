"""
HW: 2
Problem: credit card number validation
Author:Gudipudi Harikapadmini
"""


def checkisbn(num):
    """This function do the checksum task, add up all the digits by multiplying with their corresponding places"""
    tot = 0
    for i in range(len(num)):
        tot = tot + int(num[i]) * (i + 1)
    return tot % 11


if __name__ == '__main__':
    """Prints the 10-digitized credit card number, if checkisbn function returns 10 then add X at the end else add with 
    the returned value"""
    num = input('Please enter first 9 digits of an ISBN-10 as a string ')
    last_digit = checkisbn(num)
    if last_digit == 10:
        print('The ISBN-10 number is ' + num + 'X')
    else:
        print('The ISBN-10 number is ' + num + str(last_digit))
