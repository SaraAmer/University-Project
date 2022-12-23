from Src.Departments.DepartmentNode import DepartmentNode


def search_by_code(code, departments_list):
    temp = departments_list
    while temp is not None:
        if temp.get_code() == code:
            return temp
        temp = temp.get_next_node()
    return False


class Department:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_to_head(self, department_node: DepartmentNode):
        self.head = department_node
        self.size += 1

    def add_new_department(self):
        new_department_data = DepartmentNode.get_user_department_data()
        department_node = DepartmentNode(new_department_data)
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

    @staticmethod
    def search_by_name(name, collage_departments_list):
        temp = collage_departments_list
        while temp is not None:
            if temp.get_name() == name:
                return temp
            temp = temp.get_next_department()
        return False

    @staticmethod
    def update_department(collage_departments_list):
        name = input("Enter the department Name you want to update: ")
        department = Department.search_by_name(name, collage_departments_list)
        if department:
            department.update_department()
        else:
            print("Invalid Course Name Please try again")

    @staticmethod
    def delete_department(collage_departments_list):
        department_name = input("Enter the course Name you want to delete: ")
        deleted_department = Department.search_by_name(department_name, collage_departments_list)
        if deleted_department:
            collage = deleted_department.get_college()
            temp = collage.get_departments()
            if temp.get_number() == deleted_department.get_number():
                collage.set_departments(temp.get_next_department())
                return True
            while temp.get_next_department() is not None:
                if temp.get_next_department().get_number() == deleted_department.get_number():
                    temp.set_next_department(deleted_department.get_next_department())
                    deleted_department.set_next_department(None)
                    return True
                temp = temp.get_next_department()
        else:
            print("invalid department")
        return False

    def is_empty(self):
        return self.size == 0

    def choice_department(self, department_list):
        self.print_list()
        department_code = input('Enter the Department')
        department = search_by_code(department_code, department_list)
        if department:
            department.departmant_option()
        else:
            print('Please Enter A Valid Department Code')


