"""
HW:4
Problem:4
Author:Harika Padmini
"""


def Avg_salary(lines):
    avg_1, avg_2, avg_3 = 0, 0, 0
    sum1, sum2, sum3 = 0, 0, 0
    count1, count2, count3 = 0, 0, 0
    for line in lines:
        line_split = line.split()
        rank = line_split[2]
        salary = float(line_split[3])
        if rank == 'assistant':
            count1 += 1
            sum1 += salary
        elif rank == 'associate':
            count2 += 1
            sum2 += salary
        else:
            count3 += 1
            sum3 += salary
    avg_1 = round(sum1 / count1, 2)
    avg_2 = round(sum2 / count2, 2)
    avg_3 = round(sum3 / count3, 2)

    return avg_1, avg_2, avg_3, count1, count2, count3


if __name__ == '__main__':
    filename = open(r'C:\Users\harik\Downloads\Salary' + '.txt', "r")
    lines = filename.readlines()
    avg1, avg2, avg3, c1, c2, c3 = Avg_salary(lines)
    all_faculty =round( (avg1 + avg2 + avg3) / 3,2)
    print('Assistant (' + str(c1) + '): ' + '$' + str(avg1))
    print('Associate (' + str(c2) + '): ' + '$' + str(avg2))
    print('Full (' + str(c3) + '): ' + '$' + str(avg3))
    print('All Faculty (1000): ' + '$' + str(all_faculty))
