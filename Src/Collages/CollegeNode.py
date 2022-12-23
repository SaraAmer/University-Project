from Src.Departments.DepartmentNode import DepartmentNode
from Src.Departments.Department import Department
from Src.Helper import CommnFunctions


class CollegeNode:

    def __init__(self, data):
        self.__id = data['id']
        self.__name = data['name']
        self.__next_node = None
        self.__previous_node = None
        self.__students = None
        self.__departments = None

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_next_node(self):
        return self.__next_node

    def set_next_node(self, next_node):
        self.__next_node = next_node

    def get_students(self):
        return self.__students

    def set_students(self, students):
        self.__students = students

    def get_departments(self):
        return self.__departments

    def set_departments(self, departments):
        self.__departments = departments

    @staticmethod
    def get_user_college_data():
        college_data = {
            'name': input("Enter the college Name: "),
            'id': input("Enter the college id: "),

        }
        return college_data

    def update_college_data(self, data):
        self.set_name(data['name'])
        self.set_id(data['id'])

    def update_college(self):
        college_new_data = self.get_user_college_data()
        self.update_college_data(college_new_data)

    def get_last_department(self):
        temp = self.__departments
        if temp is None:
            return temp
        while temp.get_next_department() is not None:
            temp = temp.get_next_department()
        return temp

    def add_department(self):
        last_department = self.get_last_department()
        new_department_data = DepartmentNode.get_user_department_data()
        new_department = DepartmentNode(new_department_data)
        new_department.set_college(self)
        if last_department is None:
            self.__departments = new_department
        else:
            last_department.set_next_department(new_department)

    def print_collage_department(self):
        temp = self.__departments
        while temp is not None:
            print(temp.get_code() + ") " + temp.get_name())
            temp = temp.get_next_department()

    def update_collage_department(self):
        Department.update_department(self.__departments)

    def delete_collage_department(self):
        Department.delete_department(self.__departments)

    def choice_department(self):
        department = Department()
        department.choice_department(self.__departments)

    def collage_options(self):
        department = Department()
        choice = 0
        while choice != 6:
            print('1) List Collage Department')
            print('2) Choice Department')
            print('3) Add Department')
            print('4) Update Department')
            print('5) Delete Department')
            print('6) Back to Collages')
            try:
                choice = int(input('What do you want to do? '))
            except ValueError:
                print('please Enter A valid Choice')

            switcher = {
                1: self.print_collage_department,
                2: self.choice_department,
                3: self.add_department,
                4: self.update_collage_department,
                5: self.delete_collage_department
            }
            switcher.get(choice, CommnFunctions.invalid_choice)()
