"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Contract:
    def __init__(self, wage, hours):
        self.wage = wage
        self.hours = hours
        

    def get_salary_type(self):
        if(self.hours != None):
            return self.hours * self.wage
        else:
            return self.wage
    
    def get_description(self):
        if(self.hours != None):
            return f'contract of {self.hours} hours at {self.wage}/hour'
        else:
            return f'monthly salary of {self.wage}'
            

class Commission:
    def __init__(self, commission_per_contract, contracts):
        self.contracts = contracts
        self.commission_per_contract = commission_per_contract
    
    def get_commission(self):
        if(self.contracts != None):
            return self.contracts * self.commission_per_contract
        elif(self.commission_per_contract != None):
            return self.commission_per_contract
        else:
            return 0

    def get_description(self):
        if(self.contracts != None):
            return f'receives a commission for {self.contracts} contract(s) at {self.commission_per_contract}/contract'
        elif(self.commission_per_contract != None):
            return f'receives a bonus commission of {self.commission_per_contract}'
        else:
            return ''
        

class Employee:
    def __init__(self, name, contract, commission):
        self.name = name
        self.contract = contract
        self.commisssion = commission

    def get_pay(self):
        pay = 0
        pay  = self.contract.get_salary_type() + self.commisssion.get_commission()
        return pay

    def __str__(self):
        if self.contract.get_description() != '' and self.commisssion.get_description() == '':
            string = self.contract.get_description() + '.'

        elif  self.contract.get_description() != '' and self.commisssion.get_description() != '':
            string = self.contract.get_description() + ' and ' + self.commisssion.get_description()+ '.'

        elif  self.contract.get_description() == '' and self.commisssion.get_description() != '':
            string = self.commisssion.get_description()+ '.'

        # elif  self.contract.get_description() == '' and self.commisssion.get_description() == '':
        #     string = self.contract.get_description() + ' and ' + self.commisssion.get_description()+ '.'

        return f'{self.name} works on a {string}  Their total pay is {self.get_pay()}.' 


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',Contract(4000,None),Commission(None,None))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',Contract(100,25),Commission(None,None))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',Contract(3000,None),Commission(200,4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',Contract(150,25),Commission(220,3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',Contract(2000,None),Commission(1500,None))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',Contract(120,30),Commission(600,None))
