import function_with_fraction as FWF

option = "=============== OPTIONS ===============\n" \
         "1. Nhập vào một phân số mới dạng a/b.\n" \
         "2. Hiển thị danh sách phân số hiện có.\n" \
         "3. Rút gọn phân số.\n" \
         "4. Tính tổng hai phân số.\n" \
         "5. Tính tổng các phân số có trong danh sách.\n" \
         "6. Tính hiệu hai phân số.\n" \
         "7. Tính tích hai phân số.\n" \
         "8. Tính thương hai phân số.\n" \
         "9. Tính tích các phân số trong danh sách.\n" \
         "0. Thoát chương trình.\nBạn chọn? "
choose = int(input(option))
list_fraction = []
while True:
    exit = False
    match choose:
        case 1:  # Enter new fraction and save list fraction
            FWF.add_new_fraction_to_list(list_fraction)
        case 2:  # Show list fraction
            FWF.show_list_fraction(list_fraction)
        case 3:  # Reduce fraction input from keyboard
            new_fraction = FWF.reduce_fraction_from_keyboard()
            FWF.show_fraction(new_fraction)
        case 4:  # Sum two fraction from keyboard
            new_fraction = FWF.sum_two_fraction_to_keyboard()
            FWF.show_fraction(new_fraction)
        case 5:  # Sum total fraction from list fraction
            new_fraction = FWF.sum_total_fraction_to_list(list_fraction)
            FWF.show_fraction(new_fraction)
        case 6:  # Subtract two fraction from keyboard
            new_fraction = FWF.subtract_two_fraction_to_keyboard()
            FWF.show_fraction(new_fraction)
        case 7:  # Multiple two fraction from keyboard
            new_fraction = FWF.multiple_total_fraction_to_list()
            FWF.show_fraction(new_fraction)
        case 8:  # Divide two fraction from keyboard
            new_fraction = FWF.divide_two_fraction_to_keyboard()
            FWF.show_fraction(new_fraction)
        case 9:  # Multiple total fraction from keyboard
            new_fraction = FWF.multiple_total_fraction_to_list(list_fraction)
            FWF.show_fraction(new_fraction)
        case 10:  # exit program
            exit = True
            print("Thank you so much!")
        case _:
            print("syntax error!")
    if exit:
        break
    choose = int(input(option))
