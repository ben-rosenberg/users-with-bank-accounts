class BankAccount:
    all_accounts_list = []

    # Constructs new instance. Adds the instance to all accounts list
    # TODO: Add check if initial_deposit is too small (min 25)
    def __init__(self, account_name, initial_deposit, interest_rate = 0.005):
        self.account_name = account_name
        self.account_balance = initial_deposit
        self.interest_rate = interest_rate
        BankAccount.all_accounts_list.append(self)

    # Adds money to account if the amount is positive
    def deposit(self, amount):
        if amount <= 0:
            print('Cannot deposit a negative amount, make a withdrawal instead')
            return self
        self.account_balance += amount
        return self

    # Withdraws money from account if the amount is positive
    def withdraw(self, amount):
        if amount <= 0:
            print('Cannot withdraw a negative amount, make a deposit instead')
            return self
        self.account_balance -= amount
        if self.account_balance < 0:
            print('Insufficient funds: Charging $5 fee')
            self.account_balance -= 5
        return self

    # Transfer money from one account to another
    def transfer(self, other_account, amount):
        if amount <= 0:
            print('Transfer amount must be more that $0')
            return self
        self.withdraw(amount)
        other_account.deposit(amount)
        return self

    # Yields interest when account balance is positive
    def yield_interest(self):
        if (self.account_balance < 0):
            print('Account must have a positive balance in order to apply interest')
            return self
        interest_amount = self.account_balance * self.interest_rate
        self.account_balance += interest_amount
        return self

    def get_account_balance_str(self):
        return f'{self.account_name} Account Balance: ${self.account_balance}'

    # Prints the balance of all accounts
    @classmethod
    def display_all_accounts_info(cls):
        for account in cls.all_accounts_list:
            account.display_account_info()

# python bank_account.py