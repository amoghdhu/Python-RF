class Account:
    """ Simple account class with balance """

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("The amount must be greater than zero and no more then your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))


if __name__ == '__main__':
    amogh = Account("Amogh", 0)
    amogh.show_balance()

    amogh.deposit(1000)
    # tim.show_balance()
    amogh.withdraw(500)
    # tim.show_balance()

    amogh.withdraw(2000)
