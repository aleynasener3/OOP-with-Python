#Python Object-Oriented Programming

class Employee: #class
    
    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1 #since init methıd works once when new emp created

        #all the time self needed to be written init

    def fullname(self):# regular method 
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)#whether it is in class or instance, we need to use self to use variable

    #turning regular method to class method
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    #turning regular method to static method
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True
        #if you dont access the instance or the class anywhere within the function static should be used




emp_1 = Employee('corey','scahfer', 5000)#instances
emp_2= Employee('test','user', 6000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())

print(emp_1.fullname())#both are the same
print(Employee.fullname(emp_1))#when we use directly class self is needed to be defined

##tut_2 notes
# instance variables can vary but class variables are same

print(Employee.raise_amount)
print(emp_1.raise_amount)#they result same but if we use the second way, we can check if the variable has that instance

#if we change Employee.raise_amount both emp_1 and emp_2's varible will change, 
# but if we change only emp_1.raise amount there will be no change in Employee.raise_amount or emp_2.raise_amount

##tut_3
#difference between class methods and static methods
#regular methods in a class take the isnatnce as the first argument (self)

Employee.set_raise_amount(1.05)#we change all of the raise amount

#using class methods as alternative constructors
emp_str_1 = 'John-Doe-7000'
new_emp_1 = Employee.from_string(emp_str_1)

#regular class pass self 
#class methods pass cls 
#static methods dont pass anything -- logical connection

import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))

