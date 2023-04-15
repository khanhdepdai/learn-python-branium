from Student import Student


class Transcript:
    trans_id = 0
    def __init__(self, student: Student, coeficient_one= 0, coeficient_two= 0, coeficient_three= 0, gpa= 0, academic_ability= ''):
        Transcript.trans_id += 1
        self.trans_id = Transcript.trans_id
        self.student = student
        self. coeficient_one = coeficient_one
        self. coeficient_two = coeficient_two
        self. coeficient_three = coeficient_three
        self.gpa = gpa
        self.academic_ability = academic_ability


    def show_infor(self):
        print(f"Transcrip id: {self.trans_id}")
        self.student.show_info_student()
        print(f"Grade 1: {self.coeficient_one}")
        print(f"Grade 2: {self.coeficient_two}")
        print(f"Grade 3: {self.coeficient_three}")
        print(f"Gpa: {self.gpa}")
        print(f"Academic ablity: {self.academic_ability}")