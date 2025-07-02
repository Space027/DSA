class Account():
    def __init__(self,balance,withdraw,deposit,loan):
        self.balance=int(balance)
        self.withdraw=int(withdraw)
        self.deposit=int(deposit)
        self.loan=int(loan)
    def wdraw(self):
        self.balance=self.balance-self.withdraw
        if self.balance<0:
            print("TRANSACTION NOT APPROVED")
        else:
            print("TRANSACTION COMPLETED. \n",self.balance,"LEFT IN ACCOUNT.")
    def dpos(self):
        self.balance=self.balance+self.deposit
        print(self.balance,"IN ACCOUNT")
    def ln(self):
        self.balance=self.balance+self.loan
        print("YOU HAVE 30 DAYS TO REPAY",self.loan*1.1)
        print("YOU NOW HAVE",self.balance)

class Student(Account):
    def __init__(self,balance,withdraw,deposit,sloan):
        super().__init__(balance,withdraw,deposit)
        self.sloan=int(sloan)
    def sln(self):
        self.sloan=self.balance+self.loan
        self.balance=self.sloan+self.balance
        print("YOU HAVE 30 DAYS TO REPAY",self.loan*1.05)
        print("YOU NOW HAVE",self.balance)

class Savings(Account):
    def __init__(self,balance,withdraw,deposit,loan,interest):
        super().__init__(balance,withdraw,deposit,loan)
        self.interest=int(interest)
    def inter(self):
        self.interest=self.balance+self.balance*1.04
        self.balance=self.interest+self.balance
        print("CURRENT BALANCE IS",self.balance)
        print("BALANCE WILL INCREASE BY 4 PERCENT EVERY THREE MONTHS")