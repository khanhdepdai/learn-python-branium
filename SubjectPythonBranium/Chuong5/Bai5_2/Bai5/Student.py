class Student:
    student_id = 0
    def __init__(self, first_name= '', middle_name= '', last_name= '', address= '', email= '', gender= '', department= ''):
        Student.student_id += 1
        self.student_id = Student.student_id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self. gender = gender
        self.department = department


    def get_full_name(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name


    def show_info_student(self):
        print(f"Student id: {self.student_id}")
        print(f"Full name: {self.get_full_name()}")
        print(f"Adress: {self.address}")
        print(f"Email: {self.email}")
        print(f"Gender: {self.gender}")
        print(f"Departmente: {self.department}")