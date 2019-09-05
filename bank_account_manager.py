class Account:
    def __init__(self, acc_num, balance):
        self.acc_num = acc_num
        self.balance = balance

    def __str__(self):
        # shows value with two decimal numbers
        return "${}".format(round(self.balance, 2))

    def deposit(self, dep_value):
        self.balance += dep_value

    def withdraw(self, with_value):
        if self.balance > with_value:
            self.balance -= with_value
        else:
            print("Not enough funds!")


class CheckingAccount(Account):
    # creating checking account with starting balance defined by the user
    def __init__(self, acc_num, str_balance):
        super().__init__(acc_num, str_balance)

    def __str__(self):
        return "Checking account number: #{} \nBalance: {}".format(
            self.acc_num, Account.__str__(self)
        )


class SavingsAccount(Account):
    # creating savings account with starting balance defined by the user
    def __init__(self, acc_num, str_balance):
        super().__init__(acc_num, str_balance)

    def __str__(self):
        return "Savings account number: #{} \nBalance: {}".format(
            self.acc_num, Account.__str__(self)
        )


class BusinessAccount(Account):
    # creating business account with starting balance defined by the user
    def __init__(self, acc_num, str_balance):
        super().__init__(acc_num, str_balance)

    def __str__(self):
        return "Business account number: #{} \nBalance: {}".format(
            self.acc_num, Account.__str__(self)
        )
