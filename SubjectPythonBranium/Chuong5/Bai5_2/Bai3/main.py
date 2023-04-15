import function_handle_bank_account as FHBA
from BankAccount import BankAccount

option = '===================== TÙY CHỌN =====================\n' \
         '1. Thêm mới một tài khoản vào danh sách tài khoản.\n' \
         '2. Hiển thị danh sách tài khoản ra màn hình.\n' \
         '3. Nạp tiền vào tài khoản.\n' \
         '4. Rút tiền khỏi tài khoản.\n' \
         '5. Chuyển khoản.\n6. Tìm tài khoản theo tên tài khoản.\n' \
         '7. Tìm tài khoản theo số tài khoản.\n' \
         '8. Tìm tài khoản có số dư > x.\n' \
         '9. Xóa tài khoản.\n10. Sắp xếp danh sách TK theo số dư tăng dần.\n' \
         '11. Sắp xếp tài khoản theo số dư giảm dần.\n' \
         '12. Thoát chương trình.\n' \
         'Bạn chọn? '
list_acc = []
while True:
    print(option)
    choose = int(input())
    match choose:
        case 1:
            FHBA.add_acc_into_list(list_acc)
        case 2:
            FHBA.show_list_info_acc(list_acc)
        case 3:
            acc_mum = input("Enter account number if you want deposit:")
            money = int(input("Enter money if you want deposit:"))
            FHBA.deposit_money_with_num_acc(list_acc, acc_mum, money)
        case 4:
            acc_mum = input("Enter account number if you want withdraw:")
            money = int(input("Enter money if you want withdraw:"))
            FHBA.withdraw_money_with_acc_num(list_acc, acc_mum, money)
        case 5:
            acc_number_transfer = input("Enter transfer account number if you want transfer:")
            beneficiary_acc_num = input("Enter beneficiary account number if you want transfer:")
            money = int(input("Enter money if you want transfer:"))
            FHBA.transfer_money_between_two_acc(list_acc, acc_number_transfer, beneficiary_acc_num, money)
        case 6:
            name_account = input("Enter name account if you want find:")
            FHBA.find_acc_by_name_account(list_acc, name_account)
        case 7:
            name_account = input("Enter  account number if you want find:")
            FHBA.find_acc_by_account_number(list_acc, name_account)
        case 8:
            x = int(input("Enter money: "))
            FHBA.find_acc_balance_more_than_x(list_acc, x)
        case 9:
            acc_mum = input("Enter account number if you want delete: ")
            FHBA.delete_acc_by_account_number(list_acc, acc_mum)
        case 10:
            FHBA.sort_ascending_by_balance(list_acc)
        case 11:
            FHBA.sort_desc_balance_asc_name(list_acc)
        case 12:
            print("Thank you so much")
            break
        case _:
            print("INVALID")
