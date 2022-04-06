"""
Assignment name: Multiple Inheritance Assignment
Program: Manager.py
Author: Colby Boell
Last date modified: 04/05/2022

The purpose of this program is for the manager class to inherit from both the employee and the person class
to be able to use there variables and to have functions that can override the other class functions to print
out the information about the manager.
"""
from class_definitions.Employee import Employee


class Manager(Employee):
    def __init__(self, last_name, first_name, start_date, salary, department, direct_reports=[], address='', phone_number=''):
        super().__init__(last_name, first_name, start_date, salary, address='', phone_number='')
        self.department = department
        self.direct_reports = direct_reports

    def give_raise(self, salary):
        self.salary = salary

    def display(self):
        return f'Employee: {str(self.first_name)} {str(self.last_name)}\nAddress: {str(self.address)}\n' \
               f'Phone: {str(self.phone_number)}\nStart Date:{self.start_date}\n' \
               f'Salary: ${float(self.salary)}/year\nDepartment: {str(self.department)}\n' \
               f'Direct Reports: {list(self.direct_reports)}'

    def add_employees(self,direct_reports):
        self.direct_reports = direct_reports


# Driver
if __name__ == "__main__":
    m = Manager('Boell', 'Colby', '03-05-2022', 40000.00, 'Logistics')
    print(m.display())
    e = Employee('Jammin', 'Ben', '12-02-2019', 23000.00)
    e2 = Employee('Sellman', 'Mike', '03-12-2020', 23500.00)
    e3 = Employee('Kellihan', 'Lisa', '11-19-2021', 28000.00)
    emp = [e.display(), e2.display(), e3.display]
    m.add_employees(emp)
    print(m.display())
    m.give_raise(42000.00)
    print(m.display())

