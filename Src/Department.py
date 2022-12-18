import DepartmentNode


class Courses:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_to_head(self,  department_node: DepartmentNode):
        self.head = department_node
        self.size += 1

    def add_new_department(self):
        new_department_data = DepartmentNode.departmentnode.get_user_department_data()
        department_node = DepartmentNode.departmentnode(new_department_data)
        department_node.set_next_node(self.head)
        self.add_to_head(department_node)
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

    def search_by_code(self, code):
        temp = self.head
        while temp is not None:
            if temp.get_code() == code:
                return temp
            temp = temp.get_next_node()
        return False

    def update_department(self):
        name = input("Enter the department Name you want to update: ")
        department = self.search_by_name(name)
        if department:
            department.update_department()
        else:
            print("Invalid Course Name Please try again")

    def delete_department(self):
        department_name = input("Enter the course Name you want to delete: ")
        deleted_department = self.search_by_name(department_name)
        if deleted_department:
            temp = self.head
            if temp.get_code() == deleted_department.get_code():
                self.head = temp.get_next_node()
                return True
            while temp.get_next_node() is not None:
                if temp.get_next_node().get_code() == deleted_department.get_code():
                    temp.set_next_node(deleted_department.get_next_node())
                    deleted_department.set_next_node(None)
                    return True
                temp = temp.get_next_node()
        else:
            print("invalid department")
        return False

    def is_empty(self):
        return self.size == 0






#
# courseName = input("Enter the course Name you want to update")
#
# updatedCourse = Course.search_by_name(courseName)
# if updatedCourse:
#     updatedCourse.name = input("Enter the new Name you want to update")
# else:
#     print('Invalid Course')
# Course.print_list()
# courseName = input("Enter the course Name you want to delete")
# deletedCourse = Course.search_by_name(courseName)
# if deletedCourse:
#     Course.delete_course(deletedCourse)
# else:
#     print('Invalid Course')
# Course.print_list()
