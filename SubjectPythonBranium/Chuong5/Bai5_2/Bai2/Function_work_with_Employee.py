from builtins import list

from Employee import Employee


def create_new_employee() -> Employee:
    """This function create new employee and return it"""
    str_id = input("Enter id: ")
    str_first_name = input("Enter first name: ")
    str_middle_name = input("Enter midlle name: ")
    str_last_name = input("Enter last name: ")
    str_address = input("Enter address: ")
    str_age = input("Enter age: ")
    str_phone_number = input("Enter phone number: ")
    str_salary = input("Enter salary: ")
    str_experience = input("Enter experience: ")
    new_employee = Employee()
    new_employee.id = str_id
    new_employee.first_name = str_first_name
    new_employee.middle_name = str_middle_name
    new_employee.last_name = str_last_name
    new_employee.address = str_address
    new_employee.phone_number = str_phone_number
    new_employee.age = int(str_age)
    new_employee.salary = int(str_salary)
    new_employee.experience = int(str_experience)
    return new_employee


def add_new_employee_to_list(list_employee: list):
    """This functino add new employee to list """
    new_employee = create_new_employee()
    list_employee.append(new_employee)


def show_list_employee(list_employee: list):
    """This function show list employee"""
    print(f"{'ORDINAL NUMBER': ^15} |{'ID': ^15} |{'FIRST NAME': ^15} |{'MIDDLE NAME': ^15} |{'LAST NAME': ^15}" \
          f" |{'ADDRESS': ^15} |{'AGE': ^15} |{'PHONE NUMBER': ^15} |{'SALARY': ^15} |{'EXPERIENCE': ^15}")
    for i in range(len(list_employee)):
        print(
            f"{i + 1: ^15} |{list_employee[i].id: ^15} |{list_employee[i].first_name: ^15} |{list_employee[i].middle_name: ^15} |{list_employee[i].last_name: ^15} "
            f"|{list_employee[i].address: ^15} |{list_employee[i].age: ^15} |{list_employee[i].phone_number: ^15} |{list_employee[i].salary: ^15} |{list_employee[i].experience: ^15}")


def show_infor_employee(employee: Employee):
    """This function show information employee"""
    print(f"Id: {employee.id}")
    print(f"First name: {employee.first_name}")
    print(f"Middle name: {employee.middle_name}")
    print(f"Last name: {employee.last_name}")
    print(f"Address: {employee.address}")
    print(f"Age: {employee.age}")
    print(f"Phone number: {employee.phone_number}")
    print(f"Salary: {employee.salary}")
    print(f"Experience: {employee.experience}")


def find_employee_by_id(list_employee: list):
    """This function find employee by id and return infor if found or return not found"""
    id_want_find = input("Enter id if you want find")
    for i in range(len(list_employee)):
        if id_want_find.upper() == list_employee[i].id.upper():
            return show_infor_employee(list_employee[i])
    print("NOT FOUND")


def delete_employee_by_id(list_employee: list):
    """This function delete employee by id"""
    id_want_find = input("Enter id if you want find")
    for i in range(len(list_employee)):
        if id_want_find.upper() == list_employee[i].id.upper():
            list_employee.remove(list_employee[i])
            return "Delete success"
    return "NOT FOUND"


def sort_descending_by_salary(list_employee: list):
    """This function sort descending by salary"""
    for i in range(len(list_employee)):
        for i in range(len(list_employee) - 1, i, -1):
            if list_employee[i].salary > list_employee[i - 1].salary:
                list_employee[i], list_employee[i - 1] = list_employee[i - 1], list_employee[i]


def sort_ascending_by_last_name(list_employee: list):
    """This function sort ascending by name"""
    for i in range(len(list_employee)):
        for i in range(len(list_employee) - 1, i, -1):
            if list_employee[i].last_name.upper() < list_employee[i - 1].last_name.upper():
                list_employee[i], list_employee[i - 1] = list_employee[i - 1], list_employee[i]


def sort_descending_salary_and_ascending_last_name(list_employee: list):
    """This function sort ascending by salary and name"""
    for i in range(len(list_employee)):
        for i in range(len(list_employee) - 1, i, -1):
            if list_employee[i].salary > list_employee[i - 1].salary:
                list_employee[i], list_employee[i - 1] = list_employee[i - 1], list_employee[i]
            elif (list_employee[i].salary == list_employee[i - 1].salary) and (
                    list_employee[i].last_name.upper() < list_employee[i - 1].last_name.upper()):
                list_employee[i], list_employee[i - 1] = list_employee[i - 1], list_employee[i]


def show_employee_highest_salary(list_employee: list):
    """This function show employee have highest salary"""
    max = list_employee[0].salary
    for i in range(len(list_employee)):
        if max < list_employee[i].salary:
            max = list_employee[i].salary
    for i in range(len(list_employee)):
        if max == list_employee[i].salary:
            show_infor_employee(list_employee[i])


def listed_employees_same_salary(list_employee: list):
    """This function listed employees same salary"""
    for i in range(len(list_employee)):
        for j in range(i + 1, len(list_employee)):
            count = 0
            if list_employee[i].salary == list_employee[j].salary:
                count += 1
                if count == 1:
                    print(f"Employees' salary: {list_employee[i].salary}")
                print(f"{list_employee[j].id}")


def employees_same_salary_with_x(list_employee: list):
    """This function lited employee salary = x"""
    x = int(input("Enter x:"))
    for i in range(len(list_employee)):
        if x == list_employee[i].salary:
            print(f"Employees' salary is : {x}")
            print(f"{list_employee[i].id}")


def employees_have_name_is_x(list_employee: list):
    """This function listed employee'name are x"""
    x = input("Enter x:")
    for i in range(len(list_employee)):
        if x.upper() == list_employee[i].last_name.upper():
            print(f"Employees' name is : {x}")
            print(f"{list_employee[i].id}")


def employees_have_age_is_x(list_employee: list):
    """This function listed employee'age are x"""
    x = int(input("Enter x:"))
    for i in range(len(list_employee)):
        if x == list_employee[i].age:
            print(f"Employees' age is : {x}")
            print(f"{list_employee[i].id}")


def employees_have_experience_is_n(list_employee: list):
    """This function listed employee'experience are x"""
    n = int(input("Enter x:"))
    for i in range(len(list_employee)):
        if n == list_employee[i].experience:
            print(f"Employees' age is : {n}")
            print(f"{list_employee[i].id}")


def find_employee_by_three_last_phone_number(list_employee: list):
    """This function find employee by three last phone number"""
    n = input("Enter three last phone number: ")
    for i in range(len(list_employee)):
        if n == list_employee[i].phone_number[len(list_employee[i].phone_number ) - 3 : len(list_employee[i].phone_number)]:
            print(f'{list_employee[i].id}')
