"""
BankClasses program. Simulates a bank/customers/accounts/transactions/dates
"""
import doctest
from datetime import date


class MyDate:
    """
    A date object to represent a date
    """
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"


class Transaction:
    """
    Represents a single transaction. It's called with a transaction type of
    either a deposit or a withdrawal.
    If there are insufficient funds to complete the withdrawal, the
    transaction_type is set to no transaction.
    """
    TRANSACTION_DESCRIPTIONS = ["Deposit", "Withdrawal", "No transaction"]
    DEPOSIT = 0
    WITHDRAWAL = 1
    NO_TRANSACTION = 2

    def __init__(self, amount, transaction_type, date, current_balance):
        self.amount = float(amount)
        self.date = date
        self.balance_after_transaction = current_balance
        if self.amount > current_balance and transaction_type == 1:
            self.type_index = Transaction.NO_TRANSACTION
        else:
            self.type_index = transaction_type
            if self.type_index == 0:
                self.balance_after_transaction += self.amount
            else:
                self.balance_after_transaction -= self.amount
            if int(self.balance_after_transaction) == float(self.balance_after_transaction):
                self.balance_after_transaction = int(self.balance_after_transaction)
            else:
                self.balance_after_transaction = float(self.balance_after_transaction)


    def get_type_index(self):  # 0 = deposit, 1 = withdrawal, 2=no transaction
        return self.type_index

    def get_amount(self):
        return self.amount

    def get_balance_after_transaction(self):
        return self.balance_after_transaction

    def __str__(self):  # e.g. 24/1/2021 Deposit $500 Balance: $11700 or 25/1/2021 No Transaction Balance $12
        money = ""
        if not self.type_index == 2:
            money = f"${int(self.amount)} "
        return f"{self.date} {Transaction.TRANSACTION_DESCRIPTIONS[self.type_index]} {money}Balance: " \
               f"${int(self.balance_after_transaction)}"


class Account:
    """
    A bank account. Contains a list of transactions.
    """
    IS_OPEN = True
    ACCOUNT_TYPE = "GET_RICH_QUICK ACCOUNT"

    def __init__(self, id):
        self.account_id = id
        self.is_open = Account.IS_OPEN
        self.transactions = []
        self.balance = 0

    def get_is_open(self):
        return self.is_open

    def get_current_balance(self):
        return self.balance

    def set_is_open(self, set_open):
        self.is_open = set_open

    def close_account(self, close_date):
        Account.perform_transaction(self, self.balance, Transaction.WITHDRAWAL, close_date)
        self.is_open = False

    def perform_transaction(self, amount, transaction_type, date):
        current_transaction = Transaction(amount, transaction_type, date, self.balance)
        self.balance = Transaction.get_balance_after_transaction(current_transaction)
        self.transactions.append(current_transaction)
        if current_transaction.type_index == 2:
            return False
        else:
            return True

    def get_max_10_transactions(self):
        last_10_transactions = []
        if len(self.transactions) <= 10:
            last_10_transactions = self.transactions.copy()
        else:
            for i in range(1, 11):
                last_10_transactions.append(self.transactions[-i])
            last_10_transactions.reverse()

        transactions_string = ""
        if (not self.is_open) and (self.balance == 0):
            transactions_string = "dog\n"
        for i in range(len(last_10_transactions)):
            transactions_string += f"{i + 1} {last_10_transactions[i]}\n"
        return transactions_string

    def __str__(self):
        account_string = f"{self.ACCOUNT_TYPE} [{self.account_id}]: Balance ${self.balance}"
        if self.is_open == False:
            account_string = account_string + (" Account closed")
        return account_string


class Customer:
    """
    Represents a customer of a bank. They only have 1 account.
    """
    def __init__(self, person_name, person_id, account_id):
        self.name = person_name
        self.customer_id = person_id
        self.account = Account(account_id)

    def get_customer_id(self):
        return self.customer_id

    def get_name(self):
        return self.name

    def get_account_balance(self):
        return self.account.get_current_balance()

    def has_an_open_account(self):
        return self.account.get_is_open()

    def close_account(self, date):
        self.account.close_account(date)

    def open_account(self, date):
        self.account.set_is_open(True)
        self.account.perform_transaction(0, Transaction.DEPOSIT, date)

    def perform_transaction(self, amount, transaction_type, date):
        return self.account.perform_transaction(amount, transaction_type, date)

    def get_max_10_transactions(self):
        return self.account.get_max_10_transactions()

    def get_account_information(self):
        return self.account

    def __str__(self):
        customer_string = f"Name: {self.name}\nCustomer ID: {self.customer_id}\n{self.account}"
        return customer_string


class MyBank:
    """
    Represents a bank. Contains customers.
    """
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.day = date.today().strftime("%d")
        self.month = date.today().strftime("%m")
        self.year = date.today().strftime("%Y")

    def get_mydate_object(self):
        self.day = date.today().strftime("%d")
        self.month = date.today().strftime("%m")
        self.year = date.today().strftime("%Y")
        return MyDate(self.day, self.month, self.year)

    def deposit_funds(self, current_customer):
        if not current_customer.account.get_is_open():
            print("Account is closed!")
        else:
            deposit_amount = input("Enter the amount to deposit:")
            deposit_date = self.get_mydate_object()
            current_customer.account.perform_transaction(deposit_amount, Transaction.DEPOSIT, deposit_date)

    def withdraw_funds(self, current_customer):
        if not current_customer.account.IS_OPEN:
            print("Account is closed!")
        else:
            withdraw_amount = input("Enter the amount to withdraw:")
            withdraw_date = self.get_mydate_object()
            success = current_customer.account.perform_transaction(withdraw_amount, Transaction.WITHDRAWAL,
                                                                   withdraw_date)
            if not success:
                print("Not enough funds. Transaction was unsuccessful!")


    def open_account(self, current_customer):
        current_customer.open_account(self.get_mydate_object())
        print(current_customer.get_account_information)

    def close_account(self, current_customer):
        current_customer.close_account(self.get_mydate_object())
        print(current_customer.get_account_information())

    def display_bank_summary(self):
        open_accounts = 0
        total_money = 0
        for customer in self.customers:
            if customer.has_an_open_account():
                open_accounts += 1
            total_money += customer.get_account_balance()
        summary_string = f"\n************************************************************************\n" \
                         f"{self.name} has {open_accounts} customers\n" \
                         f"Total amount in customer accounts ${total_money}\n" \
                         f"************************************************************************\n"
        print(summary_string)


    def display_account_information(self, customer):
        print(customer.account)

    def display_welcome(self):
        print("Come bank with us – by Sam")

    def add_customer(self, customer):
        self.customers.append(customer)

    def remove_customer(self, customer):
        self.customers.remove(customer)


def test_bank():
    """
    # Mydate , Transaction , Account testing
    # ==== #
    # MyDate Class
    >>> date1 = MyDate(3, 12, 2021)
    >>> print(date1)
    3/12/2021

    >>> date2 = MyDate(23, 4, 2021)
    >>> print(date2)
    23/4/2021

    # ==== #
    # Transaction Class
    print("Preliminary testing of the Transaction class")
    >>> transaction = Transaction(100, Transaction.DEPOSIT, MyDate(3, 1, 2021),
    ... 3000)
    >>> print(transaction)
    3/1/2021 Deposit $100 Balance: $3100

    >>> transaction2 = Transaction(300, Transaction.WITHDRAWAL, MyDate(3, 1,
    ... 2021), 600)
    >>> print(transaction2)
    3/1/2021 Withdrawal $300 Balance: $300

    >>> transaction3 = Transaction(100.01, Transaction.WITHDRAWAL, MyDate(3, 1,
    ... 2021), 100)
    >>> print(transaction3)
    3/1/2021 No transaction Balance: $100

    # ==== #
    # Account Class
    print("Preliminary testing of the Account class")

    # -- 1 -- #
    >>> account = Account(1234)
    >>> account.perform_transaction(200, Transaction.DEPOSIT, MyDate(23, 4,
    ... 2021))
    True
    >>> print('1. Balance $' + str(account.get_current_balance()))
    1. Balance $200
    >>> account.perform_transaction(600, Transaction.DEPOSIT, MyDate(23, 4,
    ... 2021))
    True
    >>> print(account)
    GET_RICH_QUICK ACCOUNT [1234]: Balance $800

    # -- 2 -- #
    >>> account = Account(1234)

    # Transactions
    >>> account.perform_transaction(200, Transaction.DEPOSIT, MyDate(23, 4,
    ... 2021))
    True
    >>> account.perform_transaction(100, Transaction.WITHDRAWAL, MyDate(23, 4,
    ... 2021))
    True
    >>> account.perform_transaction(100.01, Transaction.WITHDRAWAL, MyDate(23,
    ... 4, 2021))
    False
    >>> account.perform_transaction(700, Transaction.DEPOSIT, MyDate(23, 4,
    ... 2021))
    True
    >>> account.perform_transaction(800, Transaction.WITHDRAWAL, MyDate(23, 4,
    ... 2021))
    True
    >>> print(account.get_max_10_transactions())
    1 23/4/2021 Deposit $200 Balance: $200
    2 23/4/2021 Withdrawal $100 Balance: $100
    3 23/4/2021 No transaction Balance: $100
    4 23/4/2021 Deposit $700 Balance: $800
    5 23/4/2021 Withdrawal $800 Balance: $0
    <BLANKLINE>

    # -- 3 -- #
    >>> print(account)
    GET_RICH_QUICK ACCOUNT [1234]: Balance $0

    # -- 4 -- #
    >>> account.close_account(MyDate(1, 1, 9999))
    >>> print(account)
    GET_RICH_QUICK ACCOUNT [1234]: Balance $0 Account closed

    # -- 5 -- #
    >>> account = Account(1234)
    >>> deposits = [35, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
    >>> for deposit in deposits:
    ...     account.perform_transaction(deposit, Transaction.DEPOSIT,
    ... MyDate(25, 4, 2021))
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    >>> print(account.get_max_10_transactions())
    1 25/4/2021 Deposit $25 Balance: $60
    2 25/4/2021 Deposit $30 Balance: $90
    3 25/4/2021 Deposit $35 Balance: $125
    4 25/4/2021 Deposit $40 Balance: $165
    5 25/4/2021 Deposit $45 Balance: $210
    6 25/4/2021 Deposit $50 Balance: $260
    7 25/4/2021 Deposit $55 Balance: $315
    8 25/4/2021 Deposit $60 Balance: $375
    9 25/4/2021 Deposit $65 Balance: $440
    10 25/4/2021 Deposit $70 Balance: $510
    <BLANKLINE>

    # Customer class

    >>> cust = Customer("Mr. Gardiner", 1, 1000)
    >>> print(cust)
    Name: Mr. Gardiner
    Customer ID: 1
    GET_RICH_QUICK ACCOUNT [1000]: Balance $0
    >>> cust.perform_transaction(1000, Transaction.DEPOSIT, MyDate(27, 2,
    ... 2022))
    True
    >>> cust.perform_transaction(300, Transaction.WITHDRAWAL, MyDate(27, 2,
    ... 2022))
    True
    >>> cust.perform_transaction(250, Transaction.WITHDRAWAL, MyDate(28, 2,
    ... 2022))
    True
    >>> cust.perform_transaction(500, Transaction.WITHDRAWAL, MyDate(1, 3,
    ... 2022))
    False
    >>> print(cust.get_max_10_transactions())
    1 27/2/2022 Deposit $1000 Balance: $1000
    2 27/2/2022 Withdrawal $300 Balance: $700
    3 28/2/2022 Withdrawal $250 Balance: $450
    4 1/3/2022 No transaction Balance: $450
    <BLANKLINE>
    >>> cust.close_account(MyDate(2, 3, 2022))
    >>> print(cust)
    Name: Mr. Gardiner
    Customer ID: 1
    GET_RICH_QUICK ACCOUNT [1000]: Balance $0 Account closed
    >>> cust.open_account(MyDate(3, 3, 2022))
    >>> print(cust.get_max_10_transactions())
    1 27/2/2022 Deposit $1000 Balance: $1000
    2 27/2/2022 Withdrawal $300 Balance: $700
    3 28/2/2022 Withdrawal $250 Balance: $450
    4 1/3/2022 No transaction Balance: $450
    5 2/3/2022 Withdrawal $450 Balance: $0
    6 3/3/2022 Deposit $0 Balance: $0
    <BLANKLINE>

    # MyBank class
    >>> take_my_money = MyBank("TakeMyMoney")
    >>> customers = []
    >>> customers.append(Customer("Mr. Gardiner", 1, 1001))
    >>> customers.append(Customer("Mr. Bean", 2, 1002))
    >>> customers.append(Customer("Gabe Newell", 3, 1003))
    >>> customers.append(Customer("Winnie the Pooh", 4, 1004))
    >>> for customer in customers:
    ...     take_my_money.add_customer(customer)
    >>> take_my_money.close_account(customers[1])
    GET_RICH_QUICK ACCOUNT [1002]: Balance $0 Account closed
    >>> import io, sys
    >>> sys.stdin = io.StringIO("500.5")  # input
    >>> take_my_money.deposit_funds(customers[0])
    Enter the amount to deposit:
    >>> take_my_money.deposit_funds(customers[1])   # Should fail
    ...                                             # Account is closed
    Account is closed!
    >>> sys.stdin = io.StringIO("600")  # input
    >>> take_my_money.deposit_funds(customers[3])   # Enter 600
    Enter the amount to deposit:
    >>> sys.stdin = io.StringIO("200")  # input
    >>> take_my_money.withdraw_funds(customers[0]) # Enter 200
    Enter the amount to withdraw:
    >>> take_my_money.display_bank_summary()
    <BLANKLINE>
    ************************************************************************
    TakeMyMoney has 3 customers
    Total amount in customer accounts $900.5
    ************************************************************************
    <BLANKLINE>
    """
    pass


doctest.testmod()  # or doctest.testmod(verbose=True)