class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        ###self.email= first + '.'+ last + '@email.com'
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete name")
        self.first = None
        self.last = None

emp_1 = Employee('John','Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())

#property decorator allows us to define a method but we can access it like an attribute

#for example if we change the name commented code wont be changed , if we change it to method we would need to change the code
##if we use property we can use like both method and attribute

#we cannot change attribute without using decorator

emp_1.fullname = 'Aleyna Sener'

## we can use code under this after we add fullname.deleter

del emp_1.fullname