class CollegeNode:

    def __init__(self, data):
        self.__id = data['id']
        self.__name = data['name']
        self.__next_node = None
        self.__previous_node = None
        self.__students = None

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



