class CourseNode:

    def __init__(self, data):
        self.__code = data['code']
        self.__name = data['name']
        self.__instructor = data['instructor']
        self.__credit_hours = data['credit_hours']
        self.__department = data['department']
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

    def set_credit_hour(self, credit_hour):
        self.__credit_hours = credit_hour

    def get_credit_hour(self):
        return  self.__credit_hours

    def set_department(self, department):
        self.__department = department

    def get_department(self):
        return self.__department

    def set_previous_node(self, previous_node):
        self.__previous_node = previous_node

    def get_previous_node(self):
        return self.__previous_node

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
            'name': input("Enter the Course Name: "),
            'code': input("Enter the Course code: "),
            'instructor': input("Enter the Course instructor: "),
            'credit_hours': input("Enter the Course credit hours: "),
            'department': input("Enter the Course department: ")
        }
        return course_data

    def update_course_data(self, data):
        self.set_name(data['name'])
        self.set_department(data['department'])
        self.set_code(data['code'])
        self.set_instructor(data['instructor'])
        self.set_credit_hour(data['credit_hours'])

    def update_course(self):
        course_new_data = self.get_user_course_data()
        self.update_course_data(course_new_data)

    def get_course_last_student(self):
        temp = self.__students
        if temp is None:
            return temp
        while temp.get_next_course() is not None:
            temp = temp.get_next_course()
        return temp

    def print_course_students(self):
        temp = self.get_students()
        while temp is not None:
            print(temp.get_student_id())
            temp = temp.get_next_student()



