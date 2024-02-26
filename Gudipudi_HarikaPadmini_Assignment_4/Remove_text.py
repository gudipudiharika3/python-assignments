"""
HW:4
Problem:1
Author:Harika Padmini
"""


def remove_all_occurrences_list(lst, element):
    return [x for x in lst if x.lower() != element.lower()]


def remove_string(file_name, removable_str):
    with open(rf'C:\Users\harik\Downloads\{file_name}', "r") as txt_file:
        lines = txt_file.readlines()
    with open(r'C:\Users\harik\Downloads\test' + '.txt', "w") as txt_file:
        for line in lines:
            new_line = remove_all_occurrences_list(line.split(), removable_str)
            txt_file.write(" ".join(new_line) + "\n")


if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    removable_str = input("Enter the string to be removed: ")
    remove_string(file_name, removable_str)
