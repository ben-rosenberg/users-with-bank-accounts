from bank_account import BankAccount


"""
A class for people with bank accounts from the BankAccount class.
"""
class User:
    def __init__(self, name, email, first_account_name, initial_deposit, interest_rate = 0.005):
        self.name = name
        self.email = email
        self.account_list = []
        self.create_new_account(first_account_name, initial_deposit, interest_rate)

    # Creates a new account and adds it to the list containing the user's accounts
    def create_new_account(self, account_name, initial_deposit, interest_rate = 0.005):
        self.account_list.append(BankAccount(account_name.upper(), initial_deposit, interest_rate))
        return self

    # Returns the account corresponding to the supplied name. Only for use in
    # other User methods, not to be called by the user. Is there an equivalent
    # to the "private" keyword in C++? Maybe this could be a staticmethod?
    def find_account_by_name(self, account_name_input):
        for account in self.account_list:
            if account_name_input.upper() == account.account_name:
                return account
        print('--------------------')
        print(f'Account named {account_name_input.upper()} not found: please enter a valid account name')
        return None

    # Calls the deposit method from the appropriate BankAccount instance. If
    # no account matches the account_name_input, returns
    def make_deposit(self, account_name_input, amount):
        this_account = self.find_account_by_name(account_name_input)
        if not this_account:
            return self
        this_account.deposit(amount)
        return self

    # Calls the withdraw method from the appropriate BankAccount instance. If
    # no account matches the account_name_input, returns
    def make_withdrawal(self, account_name_input, amount):
        this_account = self.find_account_by_name(account_name_input)
        if not this_account:
            return self
        this_account.withdraw(amount)
        return self
    
    # Calls the transfer method from the appropriate BankAccount instance.
    # It allows transfer between two accounts belonging to the same user.
    # Also checks that the supplied account names are valid. I repeat this
    # code a lot. Maybe this could be its own static method or something?
    def transfer(self, other_user, self_account_name_input, other_account_name_input, amount):
        this_self_account = self.find_account_by_name(self_account_name_input)
        this_other_account = other_user.find_account_by_name(other_account_name_input)
        if not this_self_account or not this_other_account:
            print('--------------------')
            print('Transfer could not be completed')
            return self
        this_self_account.transfer(this_other_account, amount)
        print('--------------------')
        print(f"Transfer of ${amount} from {self.name}'s {this_self_account.account_name} account to {other_user.name}'s {this_other_account.account_name} account was successful")
        return self

    # Displays the account balance. Same check of validity of the account name
    def print_account_balance(self, account_name_input):
        this_account = self.find_account_by_name(account_name_input)
        if not this_account:
            return self
        print('--------------------')
        print(f"{self.name}'s {this_account.get_account_balance_str()}")
        return self


ben = User('Ben', 'ben@email.com', 'checking', 100, 0.006)
daniel = User('Daniel', 'daniel@email.com', 'savings', 1000)

ben.make_deposit('checking', 100).print_account_balance('checking')
daniel.print_account_balance('savings')
daniel.transfer(ben, 'savings', 'checking', 500).print_account_balance('savings')
ben.print_account_balance('checking').make_withdrawal('checking', 400).print_account_balance('checking')

ben.create_new_account('savings', 100).transfer(ben, 'checking', 'savings', 100).print_account_balance('checking').print_account_balance('savings')