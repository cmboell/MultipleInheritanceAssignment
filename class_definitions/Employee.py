"""
Assignment name: Multiple Inheritance Assignment
Program: Employee.py
Author: Colby Boell
Last date modified: 04/05/2022

The purpose of this program is for the manager class to inherit from both the employee and the person class
to be able to use there variables and to have functions that can override the other class functions to print
out the information about the manager.
"""
# import
from datetime import datetime
from class_definitions.Person import Person


# Employee class
class Employee(Person):
    def __init__(self, last_name, first_name, start_date, salary, address='', phone_number=''):
        super().__init__(last_name, first_name, address='', phone_number='')
        dateformat = datetime.strptime(start_date, '%m-%d-%Y')
        self.start_date = dateformat.strftime('%m-%d-%Y')
        self.salary = salary

    def give_raise(self, salary):
        self.salary = salary

    def display(self):
        return f'Name: {str(self.first_name)} {str(self.last_name)} Start Date: {self.start_date} Salary: ${str(self.salary)}/year'
