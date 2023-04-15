class Subject:
    subject_id = 0
    def __init__(self, subject_name= '', credit= 0, num_lesson= 0, num_test= 0):
        Subject.subject_id += 1
        self.subject_id = Subject.subject_id
        self.subject_name = subject_name
        self.credit = credit
        self.num_lesson = num_lesson
        self.num_test = num_test


    def show_infor(self):
        print(f"Subject id: {self.subject_id}")
        print(f"Subject name: {self.subject_name}")
        print(f"Credit: {self.credit}")
        print(f"Number lesson: {self.num_lesson}")
        print(f"Number test: {self.num_test}")