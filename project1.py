class bankAccount:
    def __init__(self, balance,account_no):
        self.balance=balance
        self.account_no=account_no
        
    def deposite(self,amount,account_no):
        if(self.account_no==account_no):
            temp=self.balance
            self.balance=self.balance+amount
            print("Balance has been deposite to respective account no")
            print("previous balance:",temp)
            print("After deposite: ",self.balance)

    def withdraw (self,amount,account_no):
     if(self.account_no==account_no):
            temp=self.balance
            self.balance=self.balance-amount
            print("Balance has been withdraw from respective account no")
            print("previous balance:",temp)
            print("After deposite: ",self.balance)

obj=bankAccount(2000,22345)
obj.deposite(1000,22345)
obj.withdraw(500,22345)