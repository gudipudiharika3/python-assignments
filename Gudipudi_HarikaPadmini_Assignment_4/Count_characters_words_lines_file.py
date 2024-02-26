"""
HW:4
Problem:2
Author:Harika Padmini
"""


def count_lines(file_name):
    with open(rf'C:\Users\harik\Downloads\{file_name}', "r") as txt_file:
        lines = txt_file.readlines()
    return lines


def count_words(file_name):
    lines = count_lines(file_name)
    count = 0
    for line in lines:
        lst2 = line.split()
        count += len(lst2)
    return count


def count_chars(file_name):
    lst = count_lines(file_name)
    str1 = "".join(lst)
    return len(str1)


if __name__ == "__main__":
    file_name = input("Enter the filename: ")
    print(str(count_chars(file_name)) + " characters")
    print(str(count_words(file_name)) + " words")
    print(str(len(count_lines(file_name))) + " lines")
