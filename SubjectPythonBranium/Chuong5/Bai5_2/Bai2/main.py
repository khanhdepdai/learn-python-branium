import Function_work_with_Employee as FWWE


option = "========================= CÁC LỰA CHỌN =========================\n" \
         "01. Thêm mới một nhân viên vào danh sách.\n" \
         "02. Hiển thị danh sách nhân viên hiện có.\n" \
         "03. Tìm nhân viên theo mã nhân viên\n" \
         "04. Xóa nhân viên theo mã cho trước.\n" \
         "05. Sắp xếp danh sách nhân viên theo mức lương giảm dần.\n" \
         "06. Sắp xếp danh sách nhân viên theo tên tăng dần a-z.\n" \
         "07. Sắp xếp danh sách nhân viên theo lương giảm, tên tăng, họ tăng.\n" \
         "08. Liệt kê các nhân viên có lương cao nhất.\n" \
         "09. Liệt kê tất cả các nhân viên có cùng mức lương hợp đồng\n" \
         "10. Liệt kê các nhân viên có tên x nhập vào từ bàn phím.\n" \
         "11. Liệt kê các nhân viên có tuổi x nhập vào từ bàn phím.\n" \
         "12. Liệt kê các nhân viên có n năm kinh nghiệm.\n" \
         "13. Tìm nhân viên theo 3 chữ số cuối số điện thoại.\n" \
         "0. Thoát chương trình.\nBạn chọn? "
employees = []
while True:
    choice = int(input(option))
    match choice:
        case 0:
            print("Thank you so much!")
            break
        case 1:
           FWWE.add_new_employee_to_list(employees)
        case 2:
            FWWE.show_list_employee(employees)
        case 3:
            FWWE.find_employee_by_id(employees)
        case 4:
            FWWE.delete_employee_by_id(employees)
        case 5:
            FWWE.sort_descending_by_salary(employees)
        case 6:
            FWWE.sort_ascending_by_last_name(employees)
        case 7:
            FWWE.sort_descending_salary_and_ascending_last_name(employees)
        case 8:
            FWWE.show_employee_highest_salary(employees)
        case 9:
            FWWE.listed_employees_same_salary(employees)
        case 10:
            FWWE.employees_have_name_is_x(employees)
        case 11:
            FWWE.employees_have_age_is_x(employees)
        case 12:
            FWWE.employees_have_experience_is_n(employees)
        case 13:
            FWWE.find_employee_by_three_last_phone_number(employees)
        case _:
            print("ERROR!")
            break