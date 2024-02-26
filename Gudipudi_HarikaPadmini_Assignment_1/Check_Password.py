"""
HW      # 1
Problem # 1 Check Password
Author  # Gudipudi HarikaPadmini
"""


def check_password(password):
    """
    Checks if password meets minimum 8 characters. Checks all characters letters or digits and also checks total digits are minimum 2
    :param password: Input string
    :return: True if password meets above condition or False
    """
    if len(password) < 8:
        return False
    elif not password.isalnum():
        return False

    digits = 0
    for char in password:
        if char.isdigit():
            digits += 1

    if digits < 2:
        return False
    return True


if __name__ == '__main__':
    password = input("please enter the password: ")
    if check_password(password):
        print("Valid password")
    else:
        print("Invalid password")
