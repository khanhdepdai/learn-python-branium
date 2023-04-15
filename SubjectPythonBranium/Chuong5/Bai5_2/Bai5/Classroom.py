from Transcript import Transcript
from Subject import Subject


class Classroom:
    class_id = 0
    def __init__(self, class_name= '', room= '', school_time= '', subject= None):
        Classroom.class_id += 1
        self.class_id = Classroom.class_id
        self.class_name = class_name
        self.room = room
        self.school_time = school_time
        self.subject = subject
        self.transcripts = []


    def show_infor(self):
        print(f"Classroom id: {self.class_id}")
        print(f"Class name: {self.class_name}")
        print(f"Room: {self.room}")
        print(f"School time: {self.school_time}")
        self.subject.show_infor()