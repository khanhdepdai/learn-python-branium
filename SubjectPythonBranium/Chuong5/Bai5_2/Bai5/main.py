import feature

option = "=============== OPTIONS ===============\n" \
         "1. Thêm mới môn học vào danh sách môn học.\n" \
         "2. Thêm mới sinh viên vào danh sách sinh viên.\n" \
         "3. Thêm mới một lớp học vào danh sách lớp học.\n" \
         "4. Hiển thị danh sách môn học.\n" \
         "5. Hiển thị danh sách sinh viên.\n" \
         "6. Hiển thị danh sách lớp học.\n" \
         "7. Nhập và tính điểm TB cho từng sinh viên.\n" \
         "8. Xét học lực cho từng sinh viên.\n" \
         "9. Hiển thị danh sách bảng điểm.\n" \
         "10. Sắp xếp danh sách bảng điểm theo điểm TB giảm dần.\n" \
         "11. Tìm sinh viên trong lớp học theo mã sinh viên.\n" \
         "12. Cho biết các sinh viên có điểm cao nhất.\n" \
         "13. Tìm thông tin bảng điểm của sinh viên theo điểm TB.\n" \
         "14. Thoát chương trình.\n" \
         "Bạn chọn? "
choose = 0
list_subject = []
list_student = []
list_classroom = []
list_transcript = []
while True:
    print(option)
    choose = int(input())

    match choose:


        case 1:
            feature.add_new_subject_into_list(list_subject)
        case 2:
            feature.add_new_student_into_list(list_student)
        case 3:
            feature.add_new_classroom_into_list(list_classroom, list_subject)
        case 4:
            feature.show_list_subject(list_subject)
        case 5:
            feature.show_list_student(list_student)
        case 6:
            feature.show_list_classroom(list_classroom)
        case 7:
            feature.input_and_calculate_grade(list_student, list_classroom, list_transcript)
        case 8:
            feature.academic_assessment(list_transcript)
        case 9:
            for i in range(len(list_classroom)):
                print(f"Classrom {i + 1}")
                feature.show_transcript_classroom(list_classroom[i])
        case 10:
            feature.quick_sort_decs_by_gpa_acs_name(list_transcript, 0, len(list_transcript) - 1)
            for i in range(len(list_transcript)):
                print(f"{list_transcript[i].gpa} ")
        case 11:
            student_id = int(input("Enter student id: "))
            print(f"{feature.find_student_by_id(list_student, student_id)}")
        case 12:
            feature.show_students_gpa_max(list_transcript)
        case 13:
            feature.show_trans_students_by_gpa(list_transcript)
        case 14:
            print("Thank you so much!")
            break
#from 10 to 13 unedited