import datetime

class Account(object):
 

    def __init__(self, name, balance=0) -> None:
        self.name = name
        self.balance = balance
        self.transaction_history = []
    
    def trans_history(self):
        for i in self.transaction_history:
            print(self.name, "-", i)
        
        


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        history = datetime.datetime.now().strftime("%d-%m-%Y  %H:%M:%S")
        self.transaction_history.append((+amount, history))


    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance-=amount
        else:
            print("Insufficient Balance")
        history = datetime.datetime.now().strftime("%d-%m-%Y  %H:%M:%S")
        self.transaction_history.append((-amount, history))
    
    def show_balance(self):
        print(f"{self.name} - Available balance is {self.balance}")
    

tim = Account("Tim", 5000)
Tom = Account("Tom", 2000)
tim.show_balance()
Tom.show_balance()
tim.withdraw(2000)
tim.deposit(10000)
Tom.deposit(5000)
Tom.withdraw(2000)
tim.show_balance()
tim.trans_history()
Tom.trans_history()

