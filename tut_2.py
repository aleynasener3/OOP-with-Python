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

class Developer(Employee): #inherited from employee class
    raise_amount=1.10

    def __init__(self, first, last, pay,prog_lang):
        super().__init__(first, last, pay) #same thing as Employee.__init__(self,first,last,pay)
        self.prog_lang= prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay,employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

            
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Scahfer',5000,'py') #if we raise pay raise_amount will be 1.10
dev_2 = Employee('Aleyna','Sener',6000)#if we raise pay raise_amount will be 1.04

mgr_1 = Manager('Sue','smith',4000,[dev_1])

print(dev_1)
print(dev_2)

mgr_1.add_emp(dev_2)
mgr_1.print_emps()
        
print(isinstance(mgr_1,Manager)) #check if that object instance of that class
print(issubclass(Manager,Employee))#check if that class is subclass of that class