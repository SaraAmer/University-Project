class StudentNode:

    def __init__(self, data):
        self.__id = data['id']
        self.__name = data['name']
        self.__gender = data['gender']
        self.__collage = None
        self.__department = None
        self.__number = data['number']
        self.__next_node = None
        self.__previous_node = None
        self.__courses = None

    def set_id(self, student_id):
        self.__id = student_id

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_collage(self, collage):
        self.__collage = collage

    def get_collage(self):
        return self.__collage

    def set_department(self, department):
        self.__department = department

    def get_department(self):
        return self.__department

    def set_number(self, number):
        self.__number = number

    def get_number(self):
        return self.__number

    def get_next_node(self):
        return self.__next_node

    def set_next_node(self, next_node):
        self.__next_node = next_node

    def get_courses(self):
        return self.__courses

    def set_courses(self, courses):
        self.__courses = courses

    @staticmethod
    def get_user_student_data():
        student_data = {
            'id': input("Enter the Student ID: "),
            'name': input("Enter the Student Name: "),
            'gender': input("Enter the Student Gender: "),
            'number': input("Enter the Student number : ")
        }
        return student_data

    def update_student_data(self, data):
        self.set_name(data['name'])
        self.set_department(data['department'])
        self.set_id(data['id'])
        self.set_gender(data['gender'])
        self.set_collage(data['collage'])
        self.set_number(data['number'])

    def update_student(self):
        student_new_data = self.get_user_student_data()
        self.update_student_data(student_new_data)

    def get_student_last_course(self):
        temp = self.__courses
        if temp is None:
            return temp
        while temp.get_next_course() is not None:
            temp = temp.get_next_course()

        return temp

    def print_student_courses(self):
        temp = self.get_courses()
        while temp is not None:
            print(temp.get_course_code())
            temp = temp.get_next_course()




