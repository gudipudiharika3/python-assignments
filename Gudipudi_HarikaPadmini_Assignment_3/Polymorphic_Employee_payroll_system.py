from abc import ABC, abstractmethod

"""
HW      # 3
Problem # 1 Composition
Author  # Gudipudi HarikaPadmini
"""


class Employee(ABC):
    # Employee is an abstract class and have abstract methods
    def __init__(self, f_name, l_name, ssn_no):
        self._f_name = f_name
        self._l_name = l_name
        self._ssn_no = ssn_no

    def get_f_name(self):
        return self._f_name

    def get_l_name(self):
        return self._l_name

    def get_ssn_no(self):
        return self._ssn_no

    # Earnings is the abstract method and it doesnt have implementation
    @abstractmethod
    def earnings(self):
        pass

    def __str__(self):
        return f"({self._f_name},{self._l_name},{self._ssn_no})"


class SalariedEmployee(Employee):
    # This class is concrete class1
    def __init__(self, f_name, l_name, ssn_no, salary):
        super().__init__(f_name, l_name, ssn_no)
        self.salary = salary

    # getter method for salary
    def get_salary(self):
        return self.salary

    # setter method for salary
    def set_salary(self, val):
        if val >= 0:
            self.salary = val
        else:
            print("Salary cannot be negative")

    # abstract method implementation
    def earnings(self):
        return self.salary

    def __str__(self):
        return f"Salaried Employee: {super().__str__()},Earnings: ${self.salary}"


class HourlyEmployee(Employee):
    # This class is concrete class1
    def __init__(self, f_name, l_name, ssn_no, no_hrs, hrs_rate):
        super().__init__(f_name, l_name, ssn_no)
        self.no_hrs = no_hrs
        self.hrs_rate = hrs_rate

    # getter method for number of hours
    def get_no_hrs(self):
        return self.no_hrs

    # setter method for number of hours
    def set_no_hr(self, val):
        if 0 <= val <= 168:
            self.no_hrs = val
        else:
            print("The no no of hours should be in between 0 to 168")

    # getter method for hours rate
    def get_hrs_rate(self):
        return self.hrs_rate

    # setter method for hours rate
    def set_hrs_rate(self, val):
        if val >= 0:
            self.hrs_rate = val
        else:
            print("The hours rate should always greater than 0")

    # implementation of abstract class
    def earnings(self):
        if self.no_hrs <= 40:
            return self.no_hrs * self.hrs_rate
        else:
            regular_pay = 40 * self.hrs_rate
            overtime_pay = (self.no_hrs - 40) * (1.5 * self.hrs_rate)
            return float(regular_pay) + float(overtime_pay)

    def __str__(self):
        return f"Hourly Employee: {super().__str__()},Hrs: {self.no_hrs}, HoursRate: ${self.hrs_rate}"


class CommissionEmployee(Employee):
    # this is concrete class 3
    def __init__(self, f_name, l_name, ssn_no, sales, com_rate):
        super().__init__(f_name, l_name, ssn_no)
        self.sales = sales
        self.com_rate = com_rate

    # getter class for sales
    def get_sales(self):
        return self.sales

    # setter class for sales
    def set_sales(self, val):
        if val >= 0:
            self.sales = val
        else:
            print("Sales should always greater than 0")

    # getter class for commission rate
    def get_com_rate(self):
        return self.com_rate

    # setter class for commission rate
    def set_com_rate(self, val):
        if 3 <= val <= 6:
            self.com_rate = val
        else:
            print("Please enter commission in 3%-6% range")

    # implementation of concrete class
    def earnings(self):
        return self.com_rate * self.sales

    def __str__(self):
        return f"CommissionEmployee: {super().__str__()}, Commission Rate: {self.com_rate * 100}%, Sales Amounts: ${self.sales}"


if __name__ == "__main__":

    try:
        e1 = HourlyEmployee('Donald', 'Trump', '125-00-0001', 106, 26)
        e2 = CommissionEmployee('Elon', ' Musk', '125-00-0003', 100000, 6)
        e3 = SalariedEmployee('Taylor', 'Swift', '123-88-0005', 30000000)
        employee_list = [e1, e2, e3]
        for employee in employee_list:
            print(employee)
            print(f'earnings: ${employee.earnings():,.2f}')
            print()

    except ValueError as e:
        print(e)
