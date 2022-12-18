from Src.Students.StudentNode import StudentNode


class Student:
    head = None

    def __init__(self):
        self.size = 0

    def add_to_head(self, student_node: StudentNode):
        Student.head = student_node
        self.size += 1

    def add_new_student(self):
        new_student_data = StudentNode.get_user_student_data()
        student_node = StudentNode(new_student_data)
        student_node.set_next_node(Student.head)
        self.add_to_head(student_node)
        Student.print_list()

    def get_size(self):
        return self.size

    @staticmethod
    def get_head():
        return Student.head

    @staticmethod
    def search_by_name(name):
        temp = Student.head
        while temp is not None:
            if temp.get_name() == name:
                return temp
            temp = temp.get_next_node()
        return False

    @staticmethod
    def search_by_id(student_id):
        temp = Student.head
        while temp is not None:
            if temp.get_id() == student_id:
                return temp
            temp = temp.get_next_node()
        return False

    def update_student(self):
        name = input("Enter the Student Name you want to update: ")
        student = self.search_by_name(name)
        if student:
            student.update_student()
        else:
            print("Invalid Student Name Please try again")

    def delete_student(self):
        student_name = input("Enter the Student Name you want to delete: ")
        deleted_student = self.search_by_name(student_name)
        if deleted_student:
            temp = Student.head
            if temp.get_id() == deleted_student.get_id():
                Student.head = temp.get_next_node()
                return True
            while temp.get_next_node() is not None:
                if temp.get_next_node().get_id() == deleted_student.get_id():
                    temp.set_next_node(deleted_student.get_next_node())
                    deleted_student.set_next_node(None)
                    return True
                temp = temp.get_next_node()
        else:
            print("invalid student")
        return False

    @staticmethod
    def print_list():
        temp = Student.head
        while temp is not None:
            print(temp.get_name())
            temp = temp.get_next_node()

    def is_empty(self):
        return self.size == 0

    @staticmethod
    def print_student_courses():
        student_id = input("please Enter the Student id")
        student = Student.search_by_id(student_id)
        if student:
            student.print_student_courses()
        else:
            print("Invalid course code")
