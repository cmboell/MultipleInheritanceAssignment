"""
Assignment name: Multiple Inheritance Assignment
Program: Person.py
Author: Colby Boell
Last date modified: 04/05/2022

The purpose of this program is for the manager class to inherit from both the employee and the person class
to be able to use there variables and to have functions that can override the other class functions to print
out the information about the manager.
"""
# person class
class Person:
    def __init__(self, last_name, first_name, address='', phone_number=''):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.phone_number = phone_number

    def display(self):
        return f'{str(self.first_name)} {str(self.last_name)}\n{str(self.address)}\n{str(self.phone_number)}'
