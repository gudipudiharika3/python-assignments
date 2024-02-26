"""
HW:4
Problem:3
Author:Harika Padmini
"""
import random


def create_dataset(results):
    with open(r'C:\Users\harik\Downloads\Salary' + '.txt', "w") as dataset:
        dataset.writelines(results)


def get_rank(lst):
    return random.choice(lst)


def get_salary(dict1, rank):
    salary_range = dict1[rank]
    salary = random.uniform(salary_range[0], salary_range[1])
    return str(round(salary, 2))


def get_fname_lname(index):
    return "FirstName" + str(index) + " LastName" + str(index)


if __name__ == '__main__':
    results = []
    lst = ['assistant', 'associate', 'full']
    dict1 = {'assistant': [50000.00, 80000.00], 'associate': [60000.00, 110000.00], 'full': [75000.00, 130000.00]}
    for i in range(1, 1001):
        rank = get_rank(lst)
        line = get_fname_lname(i) + " " + rank + " " + get_salary(dict1, rank)+"\n"
        results.append(line)
    create_dataset(results)
