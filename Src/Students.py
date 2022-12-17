import StudentNode


class Student:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_to_head(self, student_node: StudentNode):
        self.head = student_node
        self.size += 1

    def add_new_student(self):
        new_student_data = StudentNode.StudentNode.get_user_student_data()
        student_node = StudentNode.StudentNode(new_student_data)
        student_node.set_next_node(self.head)
        self.add_to_head(student_node)
        self.print_list()

    def get_size(self):
        return self.size

    def get_head(self):
        return self.head

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.get_name())
            temp = temp.get_next_node()

    def search_by_name(self, name):
        temp = self.head
        while temp is not None:
            if temp.get_name() == name:
                return temp
            temp = temp.get_next_node()
        return False

    def search_by_id(self, student_id):
        temp = self.head
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
            temp = self.head
            if temp.get_id() == deleted_student.get_id():
                self.head = temp.get_next_node()
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

    def is_empty(self):
        return self.size == 0