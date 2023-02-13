class Employee:

    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self): #unambigupous representation of the object, used for debugging and logging
        return "Employee('{}', '{}', '{}')".format(self.first,self.last,self.pay)

    def __str__(self):#readable represenation of an object, used as a display
        return '{}-{}'.format(self.fullname(),self.email)

    def __add__(self, other):#with that instance we can add to object like emp_1+emp_2
        return self.pay+other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('corey','scahfer', 5000)#instances
emp_2= Employee('test','user', 6000)