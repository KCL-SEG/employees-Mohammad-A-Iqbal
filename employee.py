"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary_type, salary, hours, contracts, contract_rate):
        self.name = name
        self.salary_type = salary_type
        self.hours = hours
        self.salary = salary
        self.base_pay = self.salary * self.hours
        self.contracts = contracts
        self.contract_rate = contract_rate

    def get_salary_statement(self):
        if self.salary_type == 'monthly salary':
            return f"{self.salary_type} of {self.base_pay}"
        elif self.salary_type == 'contract':
            return f"{self.salary_type} of {self.hours} hours at {self.salary}/hour"
        return ''

    def get_commission(self):
        if self.contracts > 0:
            return self.contract_rate * self.contracts
        return self.contract_rate

    def get_commission_statement(self):
        if self.contract_rate == 0:
            return f"{self.get_salary_statement()}"
        elif self.contracts == 0:
            return f"{self.get_salary_statement()} and recieves a bonus commission of {self.get_commission()}"
        elif self.contracts > 0:
            return f"{self.get_salary_statement()} and recieves a commission for {self.contracts} contract(s) at {self.contract_rate}/contract"
        return ''

    def get_pay(self):
        return (self.base_pay + self.get_commission())
    
    def get_pay_statement(self):
        return f".  Their total pay is {self.get_pay()}."
         
    def __str__(self):
        return  f"{self.name} works on a {self.get_commission_statement()}{self.get_pay_statement()}"
            
            



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'monthly salary', 4000, 1, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'contract', 25, 100, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'monthly salary', 3000, 1, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'contract', 25, 150, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'monthly salary', 2000, 1, 0, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'contract', 30, 120, 0, 600)

