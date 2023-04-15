class BankAccount:
    def __init__(self, account_number="", name_account='', account_type='', balance=0, name_bank='', start_date='',
                 end_date=''):
        self.account_number = account_number
        self.name_account = name_account
        self.account_type = account_type
        self.balance = balance
        self.name_bank = name_bank
        self.start_date = start_date
        self.end_date = end_date

    def deposit_into_acc(self, money):
        """This method use deposit money into account """
        if money > 0:
            self.balance += money
            print("Deposit success.")
        else:
            print("Money invalid.")

    def withdraw_money(self, money):
        """This method use withdraw money from account if enough money"""
        if self.balance > money:
            self.balance -= money
            print("Withdraw money from account success.")
        else:
            print("Withdraw money from account failue because not enough balance.")

    def transfer(self, account: 'BankAccount', money):
        """This method transfer to other account"""
        if self.balance > money:
            self.balance -= money
            account.balance += money
            print("Transfer success.")
        else:
            print("Transfer failue because not enough balance.")

    def check_balance(self):
        """This method use check balance"""
        print(f"Balance: {self.balance}")

    def pay_service(self, money):
        """This method use pay service"""
        if self.balance > money:
            self.balance -= money
            print("Pay success.")
        else:
            print("Pay failue because not enough balance.")
