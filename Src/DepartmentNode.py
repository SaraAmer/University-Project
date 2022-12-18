class DepartmentNode:

    def __init__(self, data):
        self.__code = data['code']
        self.__name = data['name']
        self.__instructor = data['instructor']
        self.__number = data['number']
        self.__college = data['college ']
        self.__next_node = None
        self.__previous_node = None
        self.__students = None

    def set_code(self, code):
        self.__code = code

    def get_code(self):
        return self.__code

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_instructor(self, instructor):
        self.__instructor = instructor

    def get_instructor(self):
        return self.__instructor

    def set_number(self, number):
        self.__number = number

    def get_number(self):
        return  self.__number

    def set_college(self, college):
        self.__college = college

    def get_college(self):
        return self.__college

    def set_college(self, college):
        self.__college = college

    def college(self):
        return self.__college

    def get_next_node(self):
        return self.__next_node

    def set_next_node(self, next_node):
        self.__next_node = next_node

    def get_students(self):
        return self.__students

    def set_students(self, students):
        self.__students = students

    @staticmethod
    def get_user_course_data():
        course_data = {
            'name': input("Enter the department Name: "),
            'code': input("Enter the department code: "),
            'instructor': input("Enter the department instructor: "),
            'number': input("Enter the department number: "),
            'college': input("Enter the department colleget: ")
        }
        return course_data

    def update_department_data(self, data):
        self.set_name(data['name'])
        self.set_number(data['number'])
        self.set_code(data['code'])
        self.set_instructor(data['instructor'])
        self.college(data['college'])

    def update_department(self):
        course_new_data = self.get_user_course_data()
        self.update_depaetment_data(course_new_data)



