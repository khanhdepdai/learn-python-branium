class Employee:
    """This class include information and behavior of employee"""

    def __init__(self, id="id0", first_name="", middle_name="", last_name="", address="", age=0, phone_number="", salary=0, experience=""):
        """Method identity instances variable"""
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.age = age
        self.phone_number = phone_number
        self.salary = salary
        self.experience = experience

    def work(self):
        return "Work every time, every where"

    def rest(self):
        return "if tired, rest "

    def salary(self):
        return "take salary"

    def travel(self):
        return "let's travel"
