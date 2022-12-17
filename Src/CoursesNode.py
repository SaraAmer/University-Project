class CourseNode:

    def __init__(self, data):
        print(data)
        self.__code = data['code']
        self.__name = data['name']
        self.__instructor = data['instructor']
        self.__credit_hours = data['credit_hours']
        self.__department = data['department']
        self.__next_node = None
        self.__previous_node = None

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

    def set_department(self, department):
        self.__department = department

    def get_department(self):
        return self.__department

    def get_next_node(self):
        return self.__next_node

    def set_next_node(self, next_node):
        self.__next_node = next_node

    @staticmethod
    def get_user_course_data():
        course_data = {
            'name': input("Enter the Course Name"),
            'code': input("Enter the Course code"),
            'instructor': input("Enter the Course instructor"),
            'credit_hours': input("Enter the Course credit hours"),
            'department': input("Enter the Course department")
        }
        return course_data

    def update_course_data(self, data):
        self.set_name(data.name)
        self.set_department(data.department)
        self.set_code(data.code)
        self.set_instructor(data.instructor)
        self.set_credit_hour(data.credit_hours)

    def update_course(self):
        course_new_data = self.get_user_course_data()
        self.update_course_data(course_new_data)



