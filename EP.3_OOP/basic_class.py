class Employee:
    # Attribute
    # name = "loong wisawakorn"
    # position = "Software Developer"
    age = 50
    salary = 30000

    # constructor
    def __init__(self, name='name lastname', position="Free Job"):
        print("hello constructor")
        self.name = name
        self.position = position



    # method
    def code(self):
        print('I can coding, I have been working in coding for thirty years.')



class BankAccount(Employee):
    def __init__(self, money, name):
        super().__init__(name)
        self.money = money

    def deposit(self):
        self.total = self.money + Employee.salary
        print(f'ยอดเงินคงเหลือ {self.total}')

    def withdraw(self):
        self.total =  Employee.salary - self.money
        print(f'ยอดเงินคงเหลือ {self.total}')












# instance or object
emp01 = Employee("loog wisawakorn", "Developer")
emp02 = Employee("somchai", "Django Developer")
emp03 = Employee(position="free job")

print(emp01.name)
print(emp01.position)
print(emp01.age)
print("-----------------------------------------------------")
print(emp02.name)
print(emp02.position)
print(emp02.age)
print("-----------------------------------------------------")
print(emp03.name)
print(emp03.position)
print(emp03.age)

emp04 = BankAccount(3000, 'superman')

print("--------------------------inheritance---------------------------")
print(emp04.age)
print(emp04.salary)
print(emp04.name)
emp04.deposit()
emp04.withdraw()

emp05 = BankAccount(1000, 'loong wisawakorn')

print("--------------------------inheritance---------------------------")
print(emp05.age)
print(emp05.salary)
print(emp05.name)
emp05.deposit()
emp05.withdraw()



emp01.code()