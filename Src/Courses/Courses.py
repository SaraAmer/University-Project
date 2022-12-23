from Src.Courses.CoursesNode import CourseNode

class Courses:

    head = None

    def __init__(self):
        self.size = 0

    def add_to_head(self, course_node: CourseNode):
        Courses.head = course_node
        self.size += 1

    def add_new_course(self):
        new_course_data = CourseNode.get_user_course_data()
        course_node = CourseNode(new_course_data)
        course_node.set_next_node(Courses.head)
        self.add_to_head(course_node)
        self.print_list()

    def get_size(self):
        return self.size

    @staticmethod
    def get_head():
        return Courses.head

    @staticmethod
    def print_list():
        temp = Courses.head
        while temp is not None:
            print(temp.get_name())
            temp = temp.get_next_node()

    @staticmethod
    def search_by_name(name, course_list):
        temp = course_list
        while temp is not None:
            if temp.get_name() == name:
                return temp
            temp = temp.get_next_node()
        return False

    @staticmethod
    def search_by_code(code, course_list):
        temp = course_list
        while temp is not None:
            if temp.get_code() == code:
                return temp
            temp = temp.get_next_node()
        return False

    @staticmethod
    def update_course(course_list):
        name = input("Enter the Course Name you want to update: ")
        course = Courses.search_by_name(name, course_list)
        if course:
            course.update_course()
        else:
            print("Invalid Course Name Please try again")

    @staticmethod
    def delete_course(course_list):
        course_name = input("Enter the course Name you want to delete: ")
        deleted_course = Courses.search_by_name(course_name, course_list)
        if deleted_course:
            department = deleted_course.get_department()
            temp = department.get_courses()
            if temp.get_code() == deleted_course.get_code():
                department.set_courses(temp.get_next_node())
                return True
            while temp.get_next_node() is not None:
                if temp.get_next_node().get_code() == deleted_course.get_code():
                    temp.set_next_node(deleted_course.get_next_node())
                    deleted_course.set_next_node(None)
                    return True
                temp = temp.get_next_node()
        else:
            print("invalid course")
        return False

    def is_empty(self):
        return self.size == 0

    @staticmethod
    def print_course_students(course_list):
        course_code = input("please Enter the course code")
        course = Courses.search_by_code(course_code, course_list)
        if course:
            course.print_course_students()
        else:
            print("Invalid course code")




