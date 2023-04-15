from BankAccount import BankAccount


def create_acc():
    """This function create and return new account """
    number_account = input("Enter number account: ")
    name_account = input("Enter name account: ")
    type_account = input("Enter type account: ")
    balance = int(input("Enter balance: "))
    bank = input("Enter bank: ")
    start_date = input("Enter start: ")
    end_date = input("Enter end date: ")

    acc = BankAccount(number_account, name_account, type_account, balance, bank, start_date,
                      end_date)
    return acc


def add_acc_into_list(list_acc: list):
    """This function create new account and add it into list"""
    new_acc = create_acc()
    list_acc.append(new_acc)


def show_list_info_acc(list_acc: list):
    """This function show infor accounts in list with schema"""
    print(
        f"{'NUMBERICAL ORDER': ^15} {'NUMBER ACCOUNT' : ^15} {'NAME ACCOUNT' : ^15} {'TYPE ACCOUNT' : ^15} {'BALANCE' : ^15} {'BANK' : ^15} {'STRART DATE' : ^15} {'END DATE' : ^15} ")
    for i in range(len(list_acc)):
        print(
            f"{i + 1: ^15} {list_acc[i].account_number : ^15} {list_acc[i].name_account : ^15} {list_acc[i].account_type : ^15} {list_acc[i].balance : ^15} {list_acc[i].name_bank : ^15}" \
            f"{list_acc[i].start_date : ^15} {list_acc[i].end_date : ^15} ")


def deposit_money_with_num_acc(list_acc: list, acc_num, money):
    """This function deposit money into bank account by account number"""
    check = False
    for i in range(len(list_acc)):
        if list_acc[i].account_number == acc_num:
            list_acc[i].deposit_into_acc(money)
            check = True
    if check == False:
        print("Account number invalid")


def withdraw_money_with_acc_num(list_acc: list, acc_num, money):
    """This function withdraw money from account bank with account number"""
    check = False
    for i in range(len(list_acc)):
        if list_acc[i].account_number == acc_num:
            list_acc[i].withdraw_money(money)
            check = True
    if check == False:
        print("Account number invalid")


def transfer_money_between_two_acc(list_acc: list, acc_number_transfer, beneficiary_acc_num, money):
    """This function transfer money from acc_number_transfer to beneficiary_acc_num """
    check = False
    for i in range(len(list_acc)):
        if list_acc[i].account_number == acc_number_transfer:
            for j in range(len(list_acc)):
                if list_acc[j].account_number == beneficiary_acc_num:
                    list_acc[i].transfer(list_acc[j], money)
                    check = True
                    break
            break
    if check == False:
        print("Transfer account  number or beneficiary account number invarlid")


def show_info_bank_acc(bank_acc: BankAccount):
    """This function show information bank account"""
    print(f"Account number: {bank_acc.account_number}")
    print(f"Name account: {bank_acc.name_account}")
    print(f"Account type: {bank_acc.account_type}")
    print(f"Balance: {bank_acc.balance}")
    print(f"Name account: {bank_acc.name_account}")
    print(f"Name bank: {bank_acc.name_bank}")
    print(f"Start date: {bank_acc.start_date}")
    print(f"End date: {bank_acc.end_date}")
    print()


def find_acc_by_name_account(list_acc: list, name_account):
    """This function find and show information bank account by name account"""
    for i in range(len(list_acc)):
        if list_acc[i].name_account == name_account:
            show_info_bank_acc(list_acc[i])


def find_acc_by_account_number(list_acc: list, account_number):
    """This function find and show information bank account by name account"""
    for i in range(len(list_acc)):
        if list_acc[i].account_number == account_number:
            show_info_bank_acc(list_acc[i])


def find_acc_balance_more_than_x(list_acc: list, x):
    """This function find bank accounts have balacne > x"""
    for i in range(len(list_acc)):
        if list_acc[i].balance > x:
            show_info_bank_acc(list_acc[i])


def delete_acc_by_account_number(list_acc: list, acc_num):
    """This function delete bank account by account number"""
    for i in range(len(list_acc)):
        if list_acc[i].account_number == acc_num:
            list_acc.remove(list_acc[i])


def sort_ascending_by_balance(list_acc: list):
    """This function sort ascending by balance"""
    list_acc.sort(key=lambda x: x.balance)


def sort_desc_balance_asc_name(list_acc: list):
    """This function sort descending by balance if balance same, sort ascending by own name"""
    list_acc.sort(key=lambda x: (-x.balance, x.name_account))
