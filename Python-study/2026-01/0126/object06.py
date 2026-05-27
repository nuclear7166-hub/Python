class Bank:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if self__balance - amount < 0:
            print("잔액이 부족합니다.")
        else:
            self__balance = self.balance - amount
        self.showBalance()

    def deposit(self, amount):
        self__balance = self.balance + amount
        self.showBalance()

    def showBalance(self):
        print(f"현재 잔액은 {self.balance}입니다.")


account1 = Bank(1000000)
account1.showBalance()
account1.deposit(150000000000)
account1.withdraw(100000000000)
