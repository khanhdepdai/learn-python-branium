from Classroom import *
from Student import *
from Subject import *
from Transcript import *


def is_subject_exist(subject_id, list_subject: list):
    """This function check: Is Subject instance exist in list subject and return subject instance if exist, return false if not exist """
    for i in range(len(list_subject)):
        if subject_id == list_subject[i].subject_id:
            return list_subject[i]
    return False


def is_student_exist(student_id, list_student: list):
    """This function check: Is Student instance exist in list student and return Student instance if exist, return false if not exist """
    for i in range(len(list_student)):
        if student_id == list_student[i].student_id:
            return list_student[i]
    return False


def is_classroom_exist(class_id, list_class: list):
    """This function check: Is Classroom instance exist in list classroom and return Classroom instance if exist, return false if not exist """
    for i in range(len(list_class)):
        if class_id == list_class[i].class_id:
            return list_class[i]
    return False


def create_new_subject():
    """This function create new Sujbect instance"""
    subject_name = input("Enter subject name: ")
    credit = int(input("Enter credit: "))
    num_lesson = int(input("Enter number lesson: "))
    num_test = int(input("Enter number test: "))
    new_subject = Subject(subject_name, credit, num_lesson, num_test)
    return new_subject


def create_new_student():
    """This function create new Student inctance"""
    first_name = input("Enter first name: ")
    middle_name = input('Enter middle name: ')
    last_name = input('Enter last name: ')
    address = input('Enter address: ')
    email = input('Enter email: ')
    gender = input('Enter gender: ')
    department = input('Enter department: ')
    new_student = Student(first_name, middle_name, last_name, address, email, gender, department)
    return new_student


def create_new_classroom(list_subject: list):
    """This function create new Classroom instance"""
    class_name = input('Enter class name: ')
    room = input('Enter room: ')
    school_time = input('Enter school time: ')
    subject_id = int(input("Enter subject id: "))
    subject = is_subject_exist(subject_id, list_subject)
    if subject is not False:  # Check if id exist
        new_classroom = Classroom(class_name, room, school_time, subject)
        return new_classroom
    return False


def add_new_subject_into_list(list_subject: list):
    """This function create new Subject instance and add this into list subject"""
    new_subject = create_new_subject()
    new_subject.show_infor()
    list_subject.append(new_subject)


def add_new_student_into_list(list_student: list):
    """This function create new Student instance and add this into list student"""
    new_student = create_new_student()
    new_student.show_info_student()
    list_student.append(new_student)


def add_new_classroom_into_list(list_classroom: list, list_subject: list):
    """This function create new Classroom instance and add this into list"""
    new_classroom = create_new_classroom(list_subject)
    if new_classroom is False:
        print("The subject is not exist in the table subject. Create classroom falie")
    else:
        new_classroom.show_infor()
        list_classroom.append(new_classroom)


def show_list_subject(list_subject: list):
    """This function show list subject with schema"""
    print(
        f"|{'Subject id': ^15}|{'Subject name': ^15}|{'Credit': ^15}|{'Number lesson': ^15}|{'Number test': ^15} |")
    for i in range(len(list_subject)):
        print(
            f"|{list_subject[i].subject_id: ^15} {list_subject[i].subject_name: ^15}|{list_subject[i].credit: ^15}|{list_subject[i].num_lesson: ^15}" \
            f"|{list_subject[i].num_test: ^15} |")


def show_list_student(list_student: list):
    """This function show list student with schema"""
    print(
        f"|{'Student id': ^15}|{'First name': ^15}|{'Middle name': ^15}|{'Last named': ^15} | {'Address': ^15}|{'Email': ^15}|{'Gender': ^15}|{'Department': ^15}")
    for i in range(len(list_student)):
        print(
            f"|{list_student[i].student_id: ^15}|{list_student[i].first_name: ^15}|{list_student[i].middle_name: ^15}|{list_student[i].last_name: ^15}|" \
            f"{list_student[i].address: ^15}|{list_student[i].email: ^15}|{list_student[i].gender: ^15}|{list_student[i].department: ^15}|")


def show_transcript_classroom(classroom: Classroom):
    """This function show information classroom with schema"""
    print(
        f"|{'Classroom id': ^15}|{'Classroom name': ^15}|{'Room': ^15}|{'School time': ^15}|{'Subject': ^15}|{'Transcrip id': ^15}|" \
        f"{'Student id': ^15}|{'Full name': ^15}|{'Coeficient 1': ^15}|{'Coeficient 2': ^15}|{'Coeficient 3': ^15}|{'Gpa': ^15}|{'Academic ability': ^15}|")
    for i in range(len(classroom.transcripts)):
        print(
            f"|{classroom.class_id: ^15}|{classroom.class_name: ^15}|{classroom.room: ^15}|{classroom.school_time: ^15}|" \
            f"{classroom.subject.subject_name: ^15}|{classroom.transcripts[i].trans_id: ^15}|{classroom.transcripts[i].student.student_id: ^15}|" \
            f"{classroom.transcripts[i].student.get_full_name(): ^15}|{classroom.transcripts[i].coeficient_one: ^15}|{classroom.transcripts[i].coeficient_two: ^15}|" \
            f"{classroom.transcripts[i].coeficient_three: ^15}|{classroom.transcripts[i].gpa: ^15}|{classroom.transcripts[i].academic_ability: ^15}|")


def show_list_classroom(list_class: list):
    """This function show list classroom with schema"""
    print(
        f"|{'Classroom id': ^15} | {'Classroom name': ^15} | {'Room': ^15} | {'School time': ^15} | {'Subject': ^15}|")
    for i in range(len(list_class)):
        print(
            f"|{list_class[i].class_id: ^15} | {list_class[i].class_name: ^15} | {list_class[i].room: ^15} | {list_class[i].school_time: ^15} | " \
            f"{list_class[i].subject.subject_name: ^15}|")


def show_students_gpa_max(list_trans: list):
    """This function show information of students have gpa max"""
    max = find_gpa_max(list_trans)
    for i in range(len(list_trans)):
        if list_trans[i].gpa == max:
            list_trans[i].student.show_info_student()
            print()


def show_trans_students_by_gpa(list_trans: list):
    """This function show transcript of students by gpa """
    gpa = float(input("Enter gpa:"))
    for i in range(len(list_trans)):
        if list_trans[i].gpa == gpa:
            list_trans[i].show_infor()
            print()


def calculate_grade(grade1, grade2, grade3):
    return grade1 * 0.1 + grade2 * 0.2 + grade3 * 0.7


def input_and_calculate_grade(student_list: list, class_list: list, list_trans: list):
    """This fuction input grade and calculate gpa"""
    for i in range(len(student_list)):
        class_id = int(input(f"Enter class id for student have id {student_list[i].student_id}:"))
        classroom = is_classroom_exist(class_id, class_list)
        if classroom is not False:
            grade1 = float(input("Enter coeficient one:"))
            grade2 = float(input("Enter coeficient two:"))
            grade3 = float(input("Enter coeficient three:"))
            gpa = calculate_grade(grade1, grade2, grade3)
            transcript = Transcript(student_list[i], grade1, grade2, grade3, gpa)
            classroom.transcripts.append(transcript)
            list_trans.append(transcript)
        else:
            print("Classroom invalid!")
    if len(student_list) == 0:
        print("Not student yet!")


def academic_assessment(list_transcript: list):
    """This function assess academic ability"""
    for i in range(len(list_transcript)):
        if (list_transcript[i].gpa <= 10 and list_transcript[i].gpa >= 9):
            list_transcript[i].academic_ability = 'Excellent'
        elif (list_transcript[i].gpa < 9 and list_transcript[i].gpa >= 8):
            list_transcript[i].academic_ability = 'Good'
        elif (list_transcript[i].gpa < 8 and list_transcript[i].gpa >= 6.5):
            list_transcript[i].academic_ability = 'Quite'
        elif (list_transcript[i].gpa < 6.5 and list_transcript[i].gpa > 5):
            list_transcript[i].academic_ability = 'Average'
        else:
            list_transcript[i].academic_ability = 'Learn again'


def parameter(list_trans: list, left, right):
    local = left - 1  # local reach position of left pivot
    pivot = right
    for i in range(left, right):
        if list_trans[i].gpa > list_trans[pivot].gpa:
            local += 1
            list_trans[i], list_trans[local] = list_trans[local], list_trans[i]  # swap position because gpa of local less than gpa of pivot
        elif list_trans[i].gpa == list_trans[pivot].gpa:  # if gpa same,Compare name
            if list_trans[i].student.last_name < list_trans[pivot].student.last_name:
                local += 1
                list_trans[i], list_trans[local] = list_trans[local], list_trans[i]  # swap position because gpa of local less than gpa of pivot
            elif list_trans[i].student.last_name == list_trans[pivot].student.last_name:  # if last name same, compare first name
                if list_trans[i].student.first_name < list_trans[pivot].student.first_name:
                    local += 1
                    list_trans[i], list_trans[local] = list_trans[local], list_trans[i]  # swap position because gpa of local less than gpa of pivot
    list_trans[local + 1], list_trans[pivot] = list_trans[pivot], list_trans[local + 1]
    pivot = local + 1
    return pivot


def quick_sort_decs_by_gpa_acs_name(list_trans: list, left, right):
    """This function sort descending by gpa if two gpa same, sort ascending by name"""

    if left < right:
        pivot = parameter(list_trans, left, right)
        quick_sort_decs_by_gpa_acs_name(list_trans, left, pivot - 1)
        quick_sort_decs_by_gpa_acs_name(list_trans, pivot + 1, right)


def find_student_by_id(list_student: list, student_id):
    """This function find student by student id return True if found or return False if not found"""
    for i in range(len(list_student)):
        if student_id == list_student[i].student_id:
            return True
    return False


def find_gpa_max(list_trans: list):
    """This function find max gpa and return that value"""
    max = list_trans[0].gpa
    for i in range(len(list_trans)):
        if max < list_trans[i].gpa:
            max = list_trans[i].gpa
    return max


